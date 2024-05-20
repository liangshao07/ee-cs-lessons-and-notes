# README Tools



- Git
- GitHub
- CMake
- Markdown
- LaTeX
- Vim
- Shell
- Linux
- Docker
- 开发环境配置
- IDE
    - VSC
    - PyCharm
    - IDEA
- Typora







# Git

## 为什么使用 Git

Git 是一款分布式的代码版本控制工具，Linux 之父 Linus 嫌弃当时主流的中心式的版本控制工具太难用还要花钱，就自己开发出了 Git 用来维护 Linux 的版本（给大佬跪了）。

Git 的设计非常优雅，但初学者通常因为很难理解其内部逻辑因此会觉得非常难用。对 Git 不熟悉的初学者很容易出现因为误用命令将代码给控制版本控制没了的状况（好吧是我）。

但相信我，和 Vim 一样，Git 是一款你最终掌握之后会感叹“它值得！”的神器。

## 如何学习 Git

和 Vim 不同，我不建议初学者在一知半解的情况下贸然使用 Git，因为它的内部逻辑并不能熟能生巧，而是需要花时间去理解。我推荐的学习路线如下：

1. 阅读这篇 [Git tutorial](https://missing.csail.mit.edu/2020/version-control/)，视频的话可以看这个[尚硅谷Git教程](https://www.bilibili.com/video/BV1vy4y1s7k6)
2. 阅读这本开源书籍 [Pro Git](https://git-scm.com/book/en/v2) 的 Chapter1 - Chapter5，是的没错，学 Git 需要读一本书（捂脸）。
3. 此时你已经掌握了 Git 的原理和绝大部分用法，接下来就可以在实践中反复巩固 Git 的命令了。但用好它同样是一门哲学，我个人觉得这篇[如何写好 Commit Message](https://chris.beams.io/posts/git-commit/) 的博客非常值得一读。
4. 好的此时你已经爱上了 Git，你已经不满足于学会它了，你想自己实现一个 Git！巧了，我当年也有这样的想法，[这篇 tutorial](https://wyag.thb.lt/) 可以满足你！
5. 什么？光实现一个 Git 无法满足你？小伙子/小仙女有前途，巧的是我也喜欢造轮子，这两个 GitHub 项目 [build-your-own-x](https://github.com/danistefanovic/build-your-own-x) 和 [project-based-learning](https://github.com/tuvtran/project-based-learning) 收录了你能想到的各种造轮子教程，比如：自己造个编辑器、自己写个虚拟机、自己写个 docker、自己写个 TCP 等等等等。

分享一个好文[用动图展示10大Git命令](https://zhuanlan.zhihu.com/p/132573100)

分享一个可以学习git的在线游戏https://learngitbranching.js.org/?locale=zh_CN

CS61B的Git介绍视频能蛮好地学习和理解Git原理
Git Intro - Part 1 https://www.youtube.com/watch?v=yWBzCAY_5UI
Git Intro - Part 2 https://www.youtube.com/watch?v=CnMpARAOhFg
Git Intro - Part 3 https://www.youtube.com/watch?v=t0tzTcZESWk
Git Intro - Part 4 https://www.youtube.com/watch?v=ca1oCEMQGRQ
Git Intro - Part 5 https://www.youtube.com/watch?v=dZbj9gjjYv8
Git Intro - Part 6 https://www.youtube.com/watch?v=r0oHi0vXhLE

https://missing-semester-cn.github.io/2020/version-control/
分享一下 Git tutorial的中文版

分享一个很赞的学习站点 [git-scm.com](https://git-scm.com/book/zh/v2/起步-关于版本控制)

# GitHub

## GitHub 是什么

从功能上来说，GitHub 是一个在线代码托管平台。你可以将你的本地 Git 仓库托管到 GitHub 上，供多人同时开发浏览。但现如今 GitHub 的意义已远不止如此，它已经演变为一个非常活跃且资源极为丰富的开源交流社区。全世界的软件开发者在 GitHub 上分享各式各样种类繁多的开源软件。大到工业级的深度学习框架 PyTorch, TensorFlow，小到几十行的实用脚本，既有硬核的知识分享，也有保姆级的教程指导，甚至很多技术书籍也在 GitHub上开源（例如诸位正在看的这本——如果我厚着脸皮勉强称之为书的话）。闲来无事逛逛 GitHub 已经成为了我日常生活的一部分。

在 GitHub 里，星星是对一个项目至高无上的肯定，如果你觉得这本书对你有用的话，欢迎通过右上角的链接进入仓库主页献出你宝贵的星星✨。

## 如何使用 GitHub

如果你还从未在 GitHub 上建立过自己的远程仓库，也没有克隆过别人的代码，那么我建议你从 [GitHub的官方教程](https://docs.github.com/cn/get-started)开始自己的开源之旅。

如果你想时刻关注 GitHub 上一些有趣的开源项目，那么我向你重磅推荐 [HelloGitHub](https://hellogithub.com/) 这个网站以及它的同名微信公众号。它会定期收录 GitHub 上近期开始流行的或者非常有趣的开源项目，让你有机会第一时间接触各类优质资源。

GitHub 之所以成功，我想是得益于“我为人人，人人为我”的开源精神，得益于知识分享的快乐。如果你也想成为下一个万人敬仰的开源大佬，或者下一个 star 破万的项目作者。那就把你在开发过程中灵感一现的 idea 化作代码，展示在 GitHub 上吧～

不过需要提醒的是，开源社区不是法外之地，很多开源软件并不是可以随意复制分发甚至贩卖的，了解各类[开源协议](https://www.runoob.com/w3cnote/open-source-license.html)并遵守，不仅是法律的要求，更是每个开源社区成员的责任。

# CMake

## 为什么学习 CMake

CMake 是类似于 GNU make 的跨平台自动软件构建工具，使用 CMakeLists.txt 定义构建规则，相比于 make 它提供了更多的功能，在各种软件构建上广泛使用。**强烈建议学习使用 GNU Make 和熟悉 `Makefile` 后再学习 CMake**。

## 如何学习 CMake

`CMakeLists.txt` 比 `Makefile` 更为抽象，理解和使用难度也更大。现阶段很多 IDE (如 Visual Studio, CLion) 提供了自动生成 `CMakeLists.txt` 的功能，但掌握 `CMakeLists.txt` 的基本用法仍然很有必要。除了 [CMake 官方 Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html) 外，上海交通大学 IPADS 组新人培训也提供了[大约一小时的视频教程](https://www.bilibili.com/video/BV14h41187FZ)。

https://llvm.org/docs/CMakePrimer.html#ft-view
如果对如何用cmake去构建最基本的项目这个过程有了一定的了解，可以用这篇llvm社区写的cmake文档来强化对cmake里面的基本语法的理解，这个比cmake官方文档的可读性要强得多

如果要看书的话，推荐《Modern CMake for C++》，讲解还算清楚，作为入门绝对够用了，另一本工具书是《Professional CMake A Practical Guide》，可以当作字典查阅。

# Markdown



# LaTeX

## 为什么学 LaTeX

如果你需要写论文，那么请直接跳到下一节，因为你不学也得学。

LaTeX 是一种基于 TeX 的排版系统，由图灵奖得主 Lamport 开发，而 Tex 则是由 Knuth 最初开发，这两位都是计算机界的巨擘。当然开发者强并不是我们学习 LaTeX 的理由，LaTeX 和常见的所见即所得的 Word 文档最大的区别就是用户只需要关注写作的内容，而排版则完全交给软件自动完成。这让没有任何排版经验的普通人得以写出排版非常专业的论文或文章。

Berkeley 计算机系教授 Christos Papadimitriou 曾说过一句半开玩笑的话：

> Every time I read a LaTeX document, I think, wow, this must be correct!

## 如何学习 LaTeX

推荐的学习路线如下：

- LaTeX 的环境配置是个比较头疼的问题。如果你本地配置 LaTeX 环境出现了问题，可以考虑使用 [Overleaf](https://www.overleaf.com/) 这个在线 LaTeX 编辑网站。站内不仅有各种各样的 LaTeX 模版供你选择，还免去了环境配置的难题。
- 阅读下面三篇 Tutorial: [Part-1](https://www.overleaf.com/latex/learn/free-online-introduction-to-latex-part-1), [Part-2](https://www.overleaf.com/latex/learn/free-online-introduction-to-latex-part-2), [Part-3](https://www.overleaf.com/latex/learn/free-online-introduction-to-latex-part-3)。
- 学习 LaTeX 最好的方式当然是写论文，不过从一门数学课入手用 LaTeX 写作业也是一个不错的选择。

其他值得推荐的入门学习资料如下：

- 一份简短的安装 LaTeX 的介绍 [[GitHub](https://github.com/OsbertWang/install-latex-guide-zh-cn)] 或者 TEX Live 指南（texlive-zh-cn）[[PDF](https://www.tug.org/texlive/doc/texlive-zh-cn/texlive-zh-cn.pdf)] 可以帮助你完成安装和环境配置过程
- 一份（不太）简短的 LaTeX2ε 介绍（lshort-zh-cn）[[PDF](https://mirrors.ctan.org/info/lshort/chinese/lshort-zh-cn.pdf)] [[GitHub](https://github.com/CTeX-org/lshort-zh-cn)] 是由 CTEX 开发小组翻译的，可以帮助你快速准确地入门，建议通读一遍
- 刘海洋的《LaTeX 入门》，可以当作工具书来阅读，有问题再查找，跳过 CTEX 套装部分
- [现代 LaTeX 入门讲座](https://github.com/stone-zeng/latex-talk)
- [一份其实很短的 LaTeX 入门文档](https://liam.page/2014/09/08/latex-introduction/)

Markdown可以写github的readme和静态网页，但latex不能（
LaTeX的构造相对复杂，模板、图文、公式、页眉页脚，都要设置，毕竟是一种直接编译PDF的语言
Markdown就比较简单，章节、粗体、斜体什么的都比较方便，坏处是导出成PDF就不美观。此外，用过Jupyter就会发现Markdown可以拿来在代码块之间写笔记，非常方便。
但两套系统共用一套数学符号的表达方法
所以正式文档和PPT（Beamer）我用LaTeX写，日常笔记就写Markdown

算是我個人在`LaTeX`上的一點折騰的經驗, 望能夠與大家分享交流... 本地配置`LaTeX`環境主流的方式是[`TeX Live`](https://mirrors.ustc.edu.cn/CTAN/systems/texlive/)與[`MiKTeX`](https://mirrors.ustc.edu.cn/CTAN/systems/win32/miktex/), 後者自帶`TeXworks`編輯器, 遇到沒有安裝的包也可以自動安裝, 可以説是開箱即用, 而且這兩者都是跨平臺的. 這些資源基本上都可以在[`CTAN`](https://ctan.org/)及其鏡像(如[科大鏡像](https://mirrors.ustc.edu.cn/CTAN/))上找到.

# Vim

## 为什么学习 Vim

在我看来 Vim 编辑器有如下的好处：

- 让你的整个开发过程手指不需要离开键盘，而且光标的移动不需要方向键使得你的手指一直处在打字的最佳位置。
- 方便的文件切换以及面板控制可以让你同时开发多份文件甚至同一个文件的不同位置。
- Vim 的宏操作可以批量化处理重复操作（例如多行 tab，批量加双引号等等）
- Vim 是很多服务器自带的命令行编辑器，当你通过 `ssh` 连接远程服务器之后，由于没有图形界面，只能在命令行里进行开发（当然现在很多 IDE 如 PyCharm 提供了 `ssh` 插件可以解决这个问题）。
- 异常丰富的插件生态，让你拥有世界上最花里胡哨的命令行编辑器。

## 如何学习 Vim

不幸的是 Vim 的学习曲线确实相当陡峭，我花了好几个星期才慢慢适应了用 Vim 进行开发的过程。最开始你会觉得非常不适应，但一旦熬过了初始阶段，相信我，你会爱上 Vim。

Vim 的学习资料浩如烟海，但掌握它最好的方式还是将它用在日常的开发过程中，而不是一上来就去学各种花里胡哨的高级 Vim 技巧。个人推荐的学习路线如下：

- 先阅读[这篇 tutorial](https://missing.csail.mit.edu/2020/editors/)，掌握基本的 Vim 概念和使用方式，不想看英文的可以阅读[这篇教程](https://github.com/wsdjeg/vim-galore-zh_cn)。
- 用 Vim 自带的 `vimtutor` 进行练习，安装完 Vim 之后直接在命令行里输入 `vimtutor` 即可进入练习程序。
- 最后就是强迫自己使用 Vim 进行开发，IDE 里可以安装 Vim 插件。
- 等你完全适应 Vim 之后新的世界便向你敞开了大门，你可以按需配置自己的 Vim（修改 `.vimrc` 文件），网上有数不胜数的资源可以借鉴。
- 如果你想对配置 Vim 有更加深入的了解，[*Learn Vim Script the Hard Way*](https://learnvimscriptthehardway.stevelosh.com/) 是一个很好的资源。

## 关于键位映射

用 Vim 编辑代码的时候会频繁用到 ESC 和 CTRL 键, 但是这两个键都离 home row 很远, 可以把 CapsLock 键映射到 Esc 或者 Ctrl 键，让手更舒服一些。

Windows 系统可以使用 [Powertoys](https://learn.microsoft.com/en-us/windows/powertoys/) 或者 [AutoHotkey](https://www.autohotkey.com/) 重映射键位。
MacOS 系统提供了重映射键位的[设置](https://vim.fandom.com/wiki/Map_caps_lock_to_escape_in_macOS)，另外也可以使用 [Karabiner-Elements](https://karabiner-elements.pqrs.org/) 重映射。

但更佳的做法是同时将 CapsLock 映射为 Ctrl 和 Esc，点按为 Esc，按住为 Ctrl。这是不同系统下的实现方法：

- [Windows](https://gist.github.com/sedm0784/4443120)
- [MacOS](https://ke-complex-modifications.pqrs.org/#caps_lock_tapped_escape_held_left_control)
- [Linux](https://www.jianshu.com/p/6fdc0e0fb266)

## 推荐参考资料

- Neil, Drew. Practical Vim: Edit Text at the Speed of Thought. N.p., Pragmatic Bookshelf, 2015.
- Neil, Drew. Modern Vim: Craft Your Development Environment with Vim 8 and Neovim. United States, Pragmatic Bookshelf.

# Shell



# Linux





# Docker

## 为什么使用 Docker

使用别人写好的软件/工具最大的障碍是什么——必然是配环境。配环境带来的折磨会极大地消解你对软件、编程本身的兴趣。虚拟机可以解决配环境的一部分问题，但它庞大笨重，且为了某个应用的环境配置好像也不值得模拟一个全新的操作系统。

[Docker](https://www.docker.com/) 的出现让环境配置变得（或许）不再折磨。简单来说 Docker 使用轻量级的“容器”（container）而不是整个操作系统去支持一个应用的配置。应用自身连同它的环境配置被打包为一个个 image 可以自由运行在不同平台的一个个 container 中，这极大地节省了所有人的时间成本。

## 如何学习 Docker

[Docker 官方文档](https://docs.docker.com/)当然是最好的初学教材，但最好的导师一定是你自己——尝试去使用 Docker 才能享受它带来的便利。Docker 在工业界发展迅猛并已经非常成熟，你可以下载它的桌面端并使用图形界面。

当然，如果你像我一样，是一个疯狂的造轮子爱好者，那不妨自己亲手写一个[迷你 Docker](https://github.com/PKUFlyingPig/rubber-docker) 来加深理解。

[KodeKloud Docker for the Absolute Beginner](https://kodekloud.com/courses/docker-for-the-absolute-beginner/) 全面的介绍了 Docker 的基础功能，并且有大量的配套练习，同时提供免费的云环境来完成练习。其余的云相关的课程如 Kubernetes 需要付费，但个人强烈推荐：讲解非常仔细，适合从 0 开始的新手；有配套的 Kubernetes 的实验环境，不用被搭建环境劝退。

推荐《Docker 深入浅出》https://book.douban.com/subject/30486354/

推荐看看这个就好 https://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html

# 环境配置

# Scoop

## 为什么使用 Scoop

在 Windows 下，搭建开发环境一直是一个复杂且困难的问题。由于没有一个统一的标准，导致各种开发环境的安装方式差异巨大，需要付出很多不必要的时间成本。而 Scoop 可以帮助你统一安装并管理常见的开发软件，省去了手动下载安装，配置环境变量等繁琐步骤。

例如安装 python 和 nodejs 只需要执行：

```powershell
scoop install python
scoop install nodejs
```

## 安装 Scoop

Scoop 需要 [Windows PowerShell 5.1](https://aka.ms/wmf5download) 或者 [PowerShell](https://aka.ms/powershell) 作为运行环境，如果你使用的是 Windows 10 及以上版本，Windows PowerShell 是内置在系统中的。而 Windows 7 内置的 Windows PowerShell 版本过于陈旧，你需要手动安装新版本的 PowerShell。

> 由于发现很多同学在设置 Windows 用户时使用了中文用户名，导致了用户目录也变成了中文名。如果按照 Scoop 的默认方式将软件安装到用户目录下，可能会造成部分软件执行错误。所以这里推荐安装到自定义目录，如果需要其他安装方式请参考： [ScoopInstaller/Install](https://github.com/ScoopInstaller/Install)

```powershell
# 设置 PowerShell 执行策略
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# 下载安装脚本
irm get.scoop.sh -outfile 'install.ps1'
# 执行安装, --ScoopDir 参数指定 Scoop 安装路径
.\install.ps1 -ScoopDir 'C:\Scoop'
```

## 使用 Scoop

Scoop 的官方文档对于新手非常友好，相对于在此处赘述更推荐阅读 [官方文档](https://github.com/ScoopInstaller/Scoop) 或 [快速入门](https://github.com/ScoopInstaller/Scoop/wiki/Quick-Start) 。

## Q&A

### Scoop 能配置镜像源吗？

Scoop 社区仅维护安装配置，所有的软件都是从该软件官方提供的下载链接进行下载，所以无法提供镜像源。如果因为你的网络环境导致多次下载失败，那么你需要一点点 [魔法](https://csdiy.wiki/必学工具/翻墙/)。

### 为什么找不到 Java8？

原因同上，官方已不再提供 Java8 的下载链接，推荐使用 [ojdkbuild8](https://github.com/ScoopInstaller/Java/blob/master/bucket/ojdkbuild8.json) 替代。

### 我需要安装 python2 该如何操作？

对于已经过时弃用的软件，Scoop 社区会将其从 [ScoopInstaller/Main](https://github.com/ScoopInstaller/Main) 中移除并将其添加到 [ScoopInstaller/Versions](https://github.com/ScoopInstaller/Versions) 中。如果你需要这些软件的话需要手动添加 bucket：

```powershell
scoop bucket add versions
scoop install python27
```



# IDE





# Typora













