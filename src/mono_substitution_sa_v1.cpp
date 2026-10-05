// Bounded bijective substitution solver. No plaintext truth or target metadata.
// Score is a fixed public-corpus quadgram heuristic, not a posterior probability.
#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>
using Key=std::array<int,26>;
int main(int argc,char**argv){
  if(argc!=8)throw std::runtime_error("usage: model input freq seed restarts steps output");
  const int nmodel=27*27*27*27;
  std::vector<float> model(nmodel);
  std::ifstream mf(argv[1],std::ios::binary);mf.read(reinterpret_cast<char*>(model.data()),nmodel*sizeof(float));
  if(mf.gcount()!=nmodel*sizeof(float))throw std::runtime_error("bad model size");
  std::ifstream cf(argv[2]);std::vector<int> code;int v;
  while(cf>>v){if(v<0||v>26)throw std::runtime_error("bad symbol");code.push_back(v);}
  if(code.size()<4)throw std::runtime_error("short input");
  Key freq;std::ifstream ff(argv[3]);for(int&i:freq)if(!(ff>>i))throw std::runtime_error("bad frequency order");
  auto sorted=freq;std::sort(sorted.begin(),sorted.end());for(int i=0;i<26;i++)if(sorted[i]!=i)throw std::runtime_error("bad frequency permutation");
  unsigned long long seed=std::stoull(argv[4]);int restarts=std::stoi(argv[5]),steps=std::stoi(argv[6]);
  if(restarts<=0||steps<=0)throw std::runtime_error("invalid fixed budget");
  std::array<int,26> hist{};for(int c:code)if(c!=26)hist[c]++;
  Key order;std::iota(order.begin(),order.end(),0);std::stable_sort(order.begin(),order.end(),[&](int a,int b){return hist[a]>hist[b];});
  auto score=[&](const Key&k){
    double s=0;int a[4];for(int i=0;i<3;i++)a[i]=code[i]==26?26:k[code[i]];
    for(size_t i=3;i<code.size();i++){a[3]=code[i]==26?26:k[code[i]];s+=model[((a[0]*27+a[1])*27+a[2])*27+a[3]];a[0]=a[1];a[1]=a[2];a[2]=a[3];}
    return s;
  };
  auto render=[&](const Key&k){std::string t;for(int c:code)t+=(c==26?' ':char('a'+k[c]));return t;};
  std::mt19937_64 rng(seed);std::uniform_real_distribution<double> unit(0,1);Key overall{};double best=-1e300;
  std::ofstream output(argv[7]);output<<std::setprecision(17)<<"{\"seed\":"<<seed<<",\"restarts\":"<<restarts<<",\"steps\":"<<steps<<",\"trials\":[";
  for(int r=0;r<restarts;r++){
    Key k;for(int i=0;i<26;i++)k[order[i]]=freq[i];
    if(r>0){if(r%4==0)std::shuffle(k.begin(),k.end(),rng);else for(int j=0;j<6+r%9;j++)std::swap(k[rng()%26],k[rng()%26]);}
    double current=score(k),local=current;Key lk=k;
    for(int it=0;it<steps;it++){
      int a=rng()%26,b=rng()%26;if(a==b)continue;std::swap(k[a],k[b]);double next=score(k);
      double temp=std::max(.05,6.0*(1.0-double(it)/steps));
      if(next>=current||unit(rng)<std::exp((next-current)/temp))current=next;else std::swap(k[a],k[b]);
      if(current>local){local=current;lk=k;}
    }
    if(local>best){best=local;overall=lk;}
    if(r)output<<',';output<<"{\"restart\":"<<r<<",\"score\":"<<local<<",\"plain\":\""<<render(lk)<<"\",\"key\":[";
    for(int i=0;i<26;i++){if(i)output<<',';output<<lk[i];}output<<"]}";
  }
  output<<"],\"score\":"<<best<<",\"plain\":\""<<render(overall)<<"\",\"key\":[";
  for(int i=0;i<26;i++){if(i)output<<',';output<<overall[i];}output<<"],\"cipher_solved\":false}\n";
  std::cerr<<"done seed="<<seed<<" score="<<best<<"\n";
}
