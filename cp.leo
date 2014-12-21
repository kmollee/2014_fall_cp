<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<?xml-stylesheet ekr_test?>
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="lee.20141212200847.2"><vh>@settings</vh>
<v t="lee.20141212200847.3"><vh>@data qt-gui-plugin-style-sheet</vh></v>
<v t="lee.20141212200847.4"><vh>@string initial_split_orientation = horizontal</vh></v>
</v>
<v t="lee.20141207235250.40"><vh>Computer Programming Section</vh></v>
<v t="lee.20141207235250.47"><vh>@path 14</vh>
<v t="lee.20141207235250.41" a="E"><vh>week 14</vh>
<v t="lee.20141207235250.42"><vh>goal</vh></v>
<v t="lee.20141207235250.43" a="E"><vh>第一步</vh>
<v t="lee.20141207235250.44"><vh>@file guess_password_1.py</vh></v>
</v>
<v t="lee.20141207235250.45" a="E"><vh>第二步</vh>
<v t="lee.20141207235250.46" a="E"
expanded="lee.20141207235250.50,"><vh>@file guess_password_2.py</vh></v>
</v>
<v t="lee.20141207235250.55" a="E"><vh>第三步</vh>
<v t="lee.20141207235250.56" a="E"><vh>@file guess_password_3.py</vh></v>
</v>
</v>
</v>
<v t="lee.20141212200847.9"><vh>@path 15</vh>
<v t="lee.20141215164031.41"><vh>@file __init__.py</vh></v>
<v t="lee.20141212200847.11"><vh>note</vh></v>
<v t="lee.20141212201841.7"><vh>@file symbol.py</vh></v>
<v t="lee.20141212200847.12" a="E"
expanded="lee.20141212201841.4,"><vh>@file application.py</vh></v>
</v>
<v t="lee.20141215164031.44" a="E"><vh>@path 16</vh>
<v t="lee.20141215164031.103"><vh>note</vh></v>
<v t="lee.20141215164031.81" a="E"><vh>@path templates</vh>
<v t="lee.20141215164031.84"><vh>@edit base.html</vh></v>
<v t="lee.20141215164031.82"><vh>@edit index.html</vh></v>
<v t="lee.20141215164031.88"><vh>@edit personal_page.html</vh></v>
<v t="lee.20141215164031.85"><vh>@edit 404.html</vh></v>
<v t="lee.20141215164031.89"><vh>@edit form.html</vh></v>
<v t="lee.20141215164031.90"><vh>@edit nav.html</vh></v>
</v>
<v t="lee.20141215164031.46" a="E"
expanded="lee.20141215164031.50,"><vh>@file application.py</vh></v>
<v t="lee.20141221203113.40" a="E"><vh>@path static</vh>
<v t="lee.20141221203113.41" a="E"><vh>@path css</vh>
<v t="lee.20141221203113.42"><vh>@edit custom.css</vh></v>
</v>
</v>
<v t="lee.20141215164031.62" a="E"><vh>@path std</vh>
<v t="lee.20141215164031.94" a="E"
expanded="lee.20141215164031.96,"><vh>@file a40323100.py</vh></v>
<v t="lee.20141221203113.45"><vh>@edit asciisymbol.py</vh></v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="lee.20141207235250.40"></t>
<t tx="lee.20141207235250.41"></t>
<t tx="lee.20141207235250.42">建立簡單的通關密語, 從一開始的在單機上寫出,再到轉移到 cherrypy, 在 openshift 上同步</t>
<t tx="lee.20141207235250.43">在單機上寫出 通關密語

情境兩種 通關密語錯誤 以及 正確</t>
<t tx="lee.20141207235250.45">遷移到 cherrypy</t>
<t tx="lee.20141207235250.47"></t>
<t tx="lee.20141207235250.55">與 openshift 同步</t>
<t tx="lee.20141212200847.11">this is final project note

using cherrypy

need create tmp folder, to store session</t>
<t tx="lee.20141212200847.2"></t>
<t tx="lee.20141212200847.3">QSplitter::handle {
    background-color: #CAE1FF; /* lightSteelBlue1 */
}

QStackedWidget {
    /* background-color:lightpink; */
    border-color: red;
    padding: 0px;
    /* border-width: 0px; */
    /* background-color: yellow; */
}

QSplitter {
    border-color: white;
    background-color: white;
    border-style: solid;
}

QTreeWidget {
    /* These apply to the selected item, but not to editing items.*/
    background-color: #ffffec; /* Leo's traditional tree color */
    selection-color: black; /* was white */
    selection-background-color: lightgrey;
    /* font-family: SansSerif; */
    /*font-family: DejaVu Sans Mono;*/
    font-family:YaHei Mono;
    /* 標題字型大小設定 */
    font-size: 18px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
 }

/* Headline edit widgets */
QTreeWidget QLineEdit {
    background-color: cornsilk;
    selection-color: white;
    selection-background-color: blue;
    /*font-family: DejaVu Sans Mono;*/    
    font-family:YaHei Mono;
    /* 沒有特別對應字型大小 */
    font-size: 17px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The log panes */
QTextEdit {
    background-color: #f2fdff;
    selection-color: red;
    selection-background-color: blue;
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* log font 大小 */
    font-size: 17px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The body pane */
QTextEdit#richTextEdit {
    background-color: #fdf5f5; /* A kind of pink. */
    selection-color: white;
    selection-background-color: red;
    /*font-family: DejaVu Sans Mono;*/
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* 內文字型大小 */
    font-size: 18px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

QLabel {
    font-family:YaHei Mono;
    /* 下方的 Minibuffer 標題字型大小 */
    font-size: 17px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

/* Editor labels */
QLineEdit#editorLabel {
    background-color: #ffffec;
    font-family:YaHei Mono;
    /* 沒有直接對應字型大小 */
    font-size: 17px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
    border: 2px;
    margin: 2px;
}</t>
<t tx="lee.20141212200847.4">horizontal: body pane to the left
vertical: body pane on the botton</t>
<t tx="lee.20141212200847.9"></t>
<t tx="lee.20141215164031.103">使用
    python - python3.4
    web framework - cherrypy
    template engine - jinja2
    css framewrok - skeleton

程式建構
    以 application.py 作為主要架構
    std/ 資料夾底下模組則作為延伸, 延伸模組無需設定 seesion 儲存位置
    主要架構已經有設置, 以主要架構設定的 session 儲存位置為準
    會嘗試將 std/ 從 40323101~40323157 引入主要架構
    網址為 domain/403231**
    如果不存在, 則略過, 運行時此網址則導引至 404 頁面

同學們要做的事
    因此主要架構已經完成, 各位同學請完成自己的模組, 並放置在 std/ 資料夾下
    檔名請使用 a + 學號.py, class 名稱請使用 Application
    example: a40323100.py
    DONE!

範例
    以 40323100 作為範例
</t>
<t tx="lee.20141215164031.44"></t>
<t tx="lee.20141215164031.62"></t>
<t tx="lee.20141215164031.81"></t>
<t tx="lee.20141221203113.40"></t>
<t tx="lee.20141221203113.41"></t>
</tnodes>
</leo_file>
