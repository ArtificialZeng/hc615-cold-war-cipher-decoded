# HC615

## 冷战时期的密码。220 个符号。一份可以亲手验证的完整解读。

![HC615：220 个符号、22 类字形，通过一张固定替换表得到完整捷克语明文](assets/hero.svg)

[English](README.md) · **简体中文** · [Čeština](README.cs.md) · [日本語](README.ja.md)

**作者：** Zijian Zeng, PhD · **仓库：** [hc615-cold-war-cipher-decoded](https://github.com/ArtificialZeng/hc615-cold-war-cipher-decoded) · **版本：** v1.0.2

一份在公开档案目录中登记为 **“Not solved”（未解）** 的密码，现在有了完整、可审计的捷克语解读：**一张固定替换表解释全部 220 个可见符号，零改字、零空码、零位置例外。** 这个仓库让你自己检验结果。

**220 个符号 · 22 类字形 · 32 个原始分段 · 8 行 · 0 处不符**

原材料是一页**密码分析课程练习**，HC Portal 目录约定其年代为 **1952 年**，藏于捷克 *Archiv bezpečnostních složek*。明文讲述向俄斯特拉发地区派遣工作人员：Transporta 派出九位同志参加一年劳动支援。全文每一个字母都遵循同一张可逆钥表。

**状态，整理于 2026-10-05：**完整观测消息的解读与本地验证已通过。我们最后访问时，公共目录仍标注“未解”。外部专家确认、与原始课程答案的比对尚未完成；没有主张世界首次。[结论与边界](docs/CLAIMS.md)。

## 几秒钟，自己验证

安装 Python 3.9 或更新版本后，在仓库根目录运行：

```sh
python3 scripts/verify_solution.py
```

这是只用 Python 标准库的离线核验：对照明文、22 项钥表和保存的字形转录，核查哈希与已保存的搜索输出，并逐项验证 **220/220 个符号、32/32 个分段、8/8 行**。它使用随包捷克语统计缓存复算已保存的分数，无需外部 AI 服务、新训练或重新搜索。

取得原始扫描图，并要求它与记录的 SHA-256 一致：

```sh
python3 scripts/fetch_sources.py --archive-image
python3 scripts/verify_solution.py --require-source-image
```

扫描图会保存在 Git 忽略的缓存目录。哈希一致能确认文件身份；原图字形区分是否转录正确，仍可由读者逐个复核。档案图像的再分发权尚未确认，因此仓库通过原始网站获取图像，不直接打包原图像素。

## 全部明文

以下是**未经改写的求解器输出**，按原图八行排版。重音、大小写和标点没有作为原始排版被恢复。

```text
vysilaji na ostravsko nejlepsi
pracovniky chrudimska transporta
vyslala devet soudruhu na jednorocni
brigadu jsou mezi nimi clenove
celozavodniho vyboru organisace
sami se prihlasili ostrava potrebuje
brigadniky kteri maji zkusenosti z
politicke prace
```

中文大意：将优秀工作人员派往俄斯特拉发地区。Transporta 派出九位同志，参加一年劳动支援，其中包括该组织全厂委员会的成员。他们主动报名。俄斯特拉发需要具有政治工作经验的支援人员。

ASCII `chrudimska` 有两种合理的编辑性恢复：**Chrudimská Transporta**，修饰公司；或 **pracovníky Chrudimska**，指克鲁迪姆地区的工作人员，随后在 Transporta 前断句。密文字母无法决定原始重音和标点。历史拼写 **`organisace`** 原样保留。

查看[原样明文](data/solution/PLAINTEXT_ASCII.txt)、[观测钥表](data/solution/OBSERVED_GLYPH_KEY.json)与[来源记录](docs/PROVENANCE.md)。

## 怎样得到这个结果

1. **先锁定证据。** 语言推理前完成原图转录；相似字形保留独立身份；每次出现都记录原图坐标。将红色分隔线作为明确的词界假设。
2. **先校准求解器。** 六份长度结构相匹配的捷克语替换控制，在推理时隐藏答案，平均字母恢复率达到 **99.6708%**。这是控制样本上的软件表现，不是本题正确概率。
3. **执行一次预先登记的目标实验。** 经典单表替换求解器使用固定捷克语四元模型、种子 **615499**、**16 × 32768** 次移动尝试。保存的 16 次重启均得到同一篇完整明文、同一张观测 22 字形映射。
4. **独立尝试推翻答案。** 不同 AI 代理和程序审计核查原图、全文捷克语、输入完整性、所有保存的目标分数，以及全部 220 个符号的回加密。这些核查不构成外部学者背书。

明文来自求解器实际输出，没有以大模型编造的流畅文字替代。使用的是经典单表替换方法；这份成果的价值是完整解读和透明的可复现证据。[方法、配置、控制实验与限制](docs/METHODS.md)。

如需重跑完整搜索，需要 C++17 编译器：

```sh
python3 scripts/reproduce.py --controls
python3 scripts/reproduce.py --target
python3 -m unittest discover -s tests -v
```

种子与搜索预算均已保留。不同编译器或 C++ 标准库可能影响随机搜索轨迹，不承诺跨平台优化器输出逐字节相同；固定钥表的离线核验不依赖重新搜索。

## 原始网站与外部核验

- [HC Portal 615 原始目录](https://api.hcportal.eu/api/cryptograms/615)，题名 **“Unsolved cryptogram in 11 210”**。
- [原始扫描图](https://api.hcportal.eu/media/1762/14161684790141.jpg)。
- 目录提供的馆藏标记：**Archiv bezpečnostních složek · ZSGS · box BF388a · 27-19/6-099**。
- [项目负责人及相关专家：职务、公开联系方式与出处](docs/EXPERT_CONTACTS.md)。

全部可见消息都已解释。未出现的 **f、q、w、x** 对应历史密字符号仍为 **UNKNOWN**。原始重音、标点、新闻出处、发件人与收件人、课程答案钥表尚未独立恢复。16 次重启一致，不能证明数学唯一性或世界首次。

核验者最关键的两个问题是：**这一张固定钥表是否解释完整原图？所得整篇捷克语是否连贯？** 仓库保留了检验和质疑两者所需的材料。

## 许可与引用

代码、项目原创说明和第三方语言数据分别遵循相应许可，见[来源与署名](docs/PROVENANCE.md)。随包捷克语模型及可选上游语料保留 **CC BY-NC-SA 4.0** 条件。档案扫描图与上游语料下载不纳入版本文件。

引用请使用 [CITATION.cff](CITATION.cff)。对外介绍请对照 [CLAIMS.md](docs/CLAIMS.md) 中已核验的措辞，以及 [PUBLICATION_STATUS.md](docs/PUBLICATION_STATUS.md) 中的实际发布状态。

**读出全文，重新加密，逐符号检查。**

## 图文宣传材料

[中文科技报道式 Word 稿](press/HC615_冷战档案密码_科技报道图文稿.docx)包含五张原创配图和完整明文；[四语新闻稿与社交文案](press/README.md)一并提供，外部专家确认仍待完成。
