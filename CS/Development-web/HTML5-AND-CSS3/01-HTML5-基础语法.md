# web 开发简介

- HTML-内容、骨架
- CSS-排版、美化、外表
- JS-动态、交互、血液

# HTML 骨架结构

* `html`：整个网页
* `head`：网页头部，用来存放给浏览器看的信息，例如 CSS
    * `title`：网页标题
    * `style`：网页内部 CSS 样式
    * `link`：引入外部样式等
* `body`：网页主体，用来存放给用户看的信息，例如图片、文字

```html
<html>
  <head>
    <title>网页标题</title>
    <style>CSS样式<style/>
    <link rel="stylesheet" href="./my.css">
  </head>
  <body>
    网页主体
  </body>
</html>
```

> VS Code 可以快速生成骨架：在 HTML 文件（.html）中，!（英文）配合 Enter / Tab 键

## 注释

```html
<!-- 我是 HTML 注释 -->
```

> 在 VS Code 中，**添加 / 删除**注释的快捷键：**Ctrl + /** 

#  HTML 基本标签

标签总体特点：

* 标签要成对出现，中间包裹内容
* <>里面放英文字母（标签名）
* 结束标签比开始标签多 /
* 标签分类：双标签和单标签

## 标题-h

* 文字加粗
* 字号逐渐减小
* 独占一行（换行）

```html
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<h4>四级标题</h4>
<h5>五级标题</h5>
<h6>六级标题</h6>
```

> 经验
>
> 1. h1 标签在一个网页中只能用一次，用来放新闻标题或网页的 logo
> 2. h2 ~ h6 没有使用次数的限制

## 段落-p

* 独占一行
* 段落之间存在间隙

```html
<p>段落</p>
```

## 换行-br

```html
<br>
```

## 水平线-hr

```html
<hr>
```

## 文本格式化标签

- 为文本添加特殊格式，以突出重点

- 加粗、倾斜、下划线、删除线

```html
<strong>加粗</strong>
<em>倾斜</em>
<ins>下划线</ins>
<del>删除线</del>
```

> <b><i><u><s>也可以实现同样功能，但无强调语义，故不太常用。

## 插入图片-img

- `alt`：图片无法显示的时候显示的文字
- `title`：鼠标悬停在图片上面的时候显示的文字
- `width`：值为数字，没有单位
- `height`：值为数字，没有单位
- `src`：图片地址

```html
<img src="图片地址" title="这是一张图片">
```

> src用于指定图像的位置和名称，是 <img> 的必须属性。 
>
> 属性名=“值”。
>
> 属性之间用空格隔开。

## 路径

* 相对路径：从当前文件位置出发查找目标文件
* 绝对路径：从盘符出发查找目标文件，或者通过链接找到网络上的图片

### 相对路径

查找方式：从**当前文件位置**出发查找目标文件

特殊符号：

* **/** 表示进入某个文件夹里面           → `/`
* **. ** 表示当前文件所在文件夹           → `./`
* **..** 表示当前文件的上一级文件夹   → `../` 

```
/Users/liang/Downloads/同步空间/EE-CS-ME-lessons-and-notes/CS/Introduction to programming/Web
相对于 CS：
./=====CS
../====EE-CS-ME-lessons-and-notes
/Introduction to programming====Introduction to programming
```

## 超链接-a

作用：点击跳转到其他页面。 

- `href`：跳转的链接，可以绝对，也可以相对
- `target`：默认当前窗口跳转，属性值为`_blank`可实现新窗口跳转
- 开发初期，不确定跳转地址，则 href 属性值写为 **#**，表示**空链接**，页面不会跳转，在当前页面刷新一次。

```html
<a href="https://www.baidu.com/">跳转到百度</a>

<!-- 跳转到本地文件：相对路径查找 --> 
<!-- target="_blank" 新窗口跳转页面 --> 
<a href="./01-标签的写法.html" target="_blank">跳转到01-标签的写法</a>

<!-- 开发初期，不知道超链接的跳转地址，href属性值写#，表示空链接，不会跳转 -->
<a href="#">空链接</a>
```

> **href 属性值是跳转地址，是超链接的必须属性。**
>
> 超链接默认是在当前窗口跳转页面，添加 **target="_blank"** 实现**新窗口**打开页面。

## 音频-audio

- `src`：音频链接（MP3、Ogg、Wav）
- `controls`：显示音频控制面板
- `loop`：循环播放
- `autoplay`：自动播放

```html
<!-- 在 HTML5 里面，如果属性名和属性值完全一样，可以简写为一个单词 -->
<audio src="./media/music.mp3" controls loop autoplay></audio>
```

> src 为必填属性。

## 视频-video

- `src`：视频地址（MP4、WebM、0gg）
- `controls`：显示音频控制面板
- `loop`：循环播放
- `muted`：静音播放
- `autoplay`：自动播放

```html
<!-- 在浏览器中，想要自动播放，必须有 muted 属性 -->
<video src="./media/vue.mp4" controls loop muted autoplay></video>
```

>src 为必须填属性。
>
>在浏览器中，想要自动播放，必须有 muted 属性。

## 列表

布局内容排列整齐的区域。

- 无序列表
- 有序列表
- 自定义列表

### 无序列表

作用：布局排列整齐的**不需要规定顺序**的区域。

标签：ul 嵌套 li，ul 是无序列表，li 是列表条目。

```html
<ul>
  <li>第一项</li>
  <li>第二项</li>
  <li>第三项</li>
  ……
</ul>
```

### 有序列表

作用：布局排列整齐的**需要规定顺序**的区域。

标签：ol 嵌套 li，ol 是有序列表，li 是列表条目。

```html
<ol>
  <li>第一项</li>
  <li>第二项</li>
  <li>第三项</li>
  ……
</ol>
```

### 定义列表

标签：dl 嵌套 dt 和 dd，dl 是定义列表，dt 是定义列表的标题，dd 是定义列表的描述 / 详情。

```html
<dl>
  <dt>列表标题1</dt>
  <dd>列表描述2 / 详情</dd>
  <dt>列表标题2</dt>
  <dd>列表描述2 / 详情</dd>
   ……
</dl>
```

![1680315652403](./assets/1680315652403.png)

## 表格-table

标签：table 嵌套 tr，tr 嵌套 td / th。 

- `tr`：行
- `th`：表头，即行标题
- `td`：内容
- 一行一行写，第一行表示标题

```html
<table border="1">
  <tr>
    <th>姓名</th>
    <th>语文</th>
    <th>数学</th>
    <th>总分</th>
  </tr>
  <tr>
    <td>张三</td>
    <td>99</td>
    <td>100</td>
    <td>199</td>
  </tr>
  <tr>
    <td>李四</td>
    <td>98</td>
    <td>100</td>
    <td>198</td>
  </tr>
  <tr>
    <td>总结</td>
    <td>全市第一</td>
    <td>全市第一</td>
    <td>全市第一</td>
  </tr>
</table>
```

> 提示：在网页中，**表格默认没有边框线**，使用 **border 属性**可以为表格添加边框线。 

### 合并单元格

合并单元格的步骤：

1. 明确合并的目标
2. 保留**最左最上**的单元格，添加属性（取值是**数字**，表示需要**合并的单元格数量**）
    * **跨行合并**，保留最上单元格，添加属性 **rowspan**
    * **跨列合并**，保留最左单元格，添加属性 **colspan**
3. 删除其他单元格

```html
<table border="1">
  <thead>
    <tr>
      <th>姓名</th>
      <th>语文</th>
      <th>数学</th>
      <th>总分</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>张三</td>
      <td>99</td>
      <td rowspan="2">100</td>
      <td>199</td>
    </tr>
    <tr>
      <td>李四</td>
      <td>98</td>
      <!-- <td>100</td> -->
      <td>198</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>总结</td>
      <td colspan="3">全市第一</td>
      <!-- <td>全市第一</td>
      <td>全市第一</td> -->
    </tr>
  </tfoot>
</table>
```

## 表单-form

作用：收集用户信息。

使用场景：

* 登录页面
* 注册页面
* 搜索区域

表单域标签下，下面的标签才起作用。

### input

- `type`：type 属性值不同，则功能不同
    - `text`：文本框
        - `placeholder`：提示信息
    - `password`：密码框
        - `placeholder`：提示信息
    - `radio`：单选框
        - `name`：控件名称，控件分组，同组只能选中一个（单选功能）
        - `checked`：默认选中 属性名和属性值相同，简写为一个单词
    - `checkbox`：多选框
        - `checked`：默认选中 属性名和属性值相同，简写为一个单词
    - `file`：上传文件
        - `multiple`：文件多选

```html
<input type="..." placeholder="提示信息">

<input type="radio" name="gender" checked> 男
<input type="radio" name="gender"> 女

<input type="checkbox" checked> 敲前端代码

<input type="file" multiple>
```

### 下拉菜单-select

- `select` 嵌套 `option`
- `select` 是下拉菜单整体
- `option`是下拉菜单的每一项
- `selected`：默认选中属性

```html
<select>
  <option>北京</option>
  <option>上海</option>
  <option>广州</option>
  <option>深圳</option>
  <option selected>武汉</option>
</select>
```

### 文本域-textarea

多行文本表单控件。

```html
<textarea>默认提示文字</textarea>
```

> 注意点：
>
> * 实际开发中，使用 CSS 设置 文本域的尺寸
> * 实际开发中，一般禁用右下角的拖拽功能

### 标签-label

经验：用 label 标签绑定文字和表单控件的关系，增大表单控件的点击范围。 

* 写法一
    * label 标签只包裹内容，不包裹表单控件
    * 设置 label 标签的 for 属性值 和表单控件的 id 属性值相同

```html
<input type="radio" id="man">
<label for="man">男</label>
```

* 写法二：使用 label 标签包裹文字和表单控件，不需要属性 

```html
<label><input type="radio"> 女</label>
```

> 提示：支持 label 标签增大点击范围的表单控件：文本框、密码框、上传文件、单选框、多选框、下拉菜单、文本域等等。 

### 按钮-button

- `submit`：提交按钮，点击后可以提交数据到后台（默认功能）
- `reset`：重置按钮，点击后将表单控件恢复默认值
- `button`：普通按钮，默认没有功能，一般配合JavaScript 使用

```html
<!-- form 表单区域 -->
<!-- action="" 发送数据的地址 -->
<form action="">
  用户名：<input type="text">
  <br><br>
  密码：<input type="password">
  <br><br>

  <!-- 如果省略 type 属性，功能是 提交 -->
  <button type="submit">提交</button>
  <button type="reset">重置</button>
  <button type="button">普通按钮</button>
</form>
```

## 语义化-布局标签-div

- 无语义
    - `div`：独占一行
    - `span`：不换行
- 有语义
    - `header`：头部
    - `nav`：导航
    - `footer`：底部
    - `aside`：侧边栏
    - `section`：区块
    - `article`：文章

















