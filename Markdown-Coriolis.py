#!/usr/bin/env python
# coding: utf-8

# In[181]:


def praeambel():
    pra_text="""<style type=\"text/css\">
    @page{
        size: A4;
    }
    div.bg{
        -webkit-print-color-adjust: exact;
        background-color:blue;
        background-image: url(bg-coriolis.jpg);
        background-size:     cover;
        background-repeat:   no-repeat;
        background-position: center center;
        width:21cm;height:29.7cm;
        border:1px solid blue;
        padding:20px;
    }
    body{
        height: 29.7cm;
        width=21cm;
        color:#40FF00;
        margin-left=auto;
        margin-right=auto;
        text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;

    }
    h1{
        color: #585858;
        text-shadow: -2px 0 silver, 0 2px silver, 2px 0 silver, 0 -2px silver;
    }
    h2{
        color: black;
        text-shadow: -2px 0 silver, 0 2px silver, 2px 0 silver, 0 -2px silver;
    }
    </style>
    """
    return pra_text

def start_text():
    start_html="""
    <body>
    <div class=bg>
    """
    return start_html

def closing():
    close_text="""</div></body>"""
    return close_text


# In[186]:


def convert_to_hash(line):
    count=0
    for char in line:
        if(char!="#"):
            break
        if(char=="#"):
            count+=1
    if(count>0):
        new_line="<h"+str(count)+">"+line[count+1:].strip()+"</h"+str(count)+">"
    return new_line

def convert_to_bullet(line):
    new_line="<ul><li>"+line[1:].strip()+"</li></ul>"
    return new_line

def insert_italic(line):
    italic_ind=line.find("_")
    is_there=True
    if(italic_ind!=None):
        next_italic=line.find("_", italic_ind+1)
        if(next_italic!=-1 and next_italic!=0):
            line=line[:italic_ind-1]+" <em>"+line[italic_ind+1:next_italic]+"</em> "+line[next_italic+2:]
        elif(next_italic==0):
            line="<em>"+line[italic_ind+1:next_italic]+"</em> "+line[next_italic+2:]
        else:
            is_there=False
    else:
        is_there=False
    return line, is_there

def insert_bold(line):
    bold_ind=line.find("**")
    is_there=True
    if(bold_ind!=None):
        next_bold=line.find("**", bold_ind+1)
        if(next_bold!=-1):
            line=line[:bold_ind-1]+" <strong>"+line[bold_ind+2:next_bold]+"</strong> "+line[next_bold+2:]
        else:
            is_there=False
    else:
        is_there=False
    return line, is_there

def look_for_special_char(line):
    is_there = False
    if("_" in line):
        line, is_there=insert_italic(line)
    elif("**" in line):
        line, is_there=insert_bold(line)
    return line, is_there


def markdown(string):
    #lines=string.splitlines()
    new_text=""
    line=string
    #for line in lines:
    #if(len(line)==0):
    if(line=="\n"):
        new_line="<br>"
    elif(line[0]=="#"):
        new_line=convert_to_hash(line)
    elif(line[0]=="*"):
        new_line=convert_to_bullet(line)
    elif(line[:5]=="\page"):
        new_line=closing()+"\n\n"+start_text()
    else:
        is_there=True
        count=0
        while(is_there):
            line, is_there=look_for_special_char(line)
            count+=1
            if(count>10):
                break
        new_line=line
    #new_text.append(new_line)
    #new_text=new_text+" \n "+new_line
    return new_line


# In[190]:


test="""# sub heading
## sub sub heading #
### blub
asdsad sd _asasd_ sakdhsa _asd_
her eise some **bold** text

* item1
* item2 *
* item3
\page

sdsadsadsdsadlnsaldn sadnksandlknsald saldnmsadlkadnsa snflkdnflksnd sadnsakndsandlsandndslkd sadnsadlksadsad sadmsaödmöadmksad """
new=[]
new.append(praeambel())
new.append(start_text())

f = open("Story.txt", "r")
for x in f:
    new.append(markdown(x))

new.append(closing())


# In[191]:


f=open("blubs.html","w+")
for entry in new:
    f.write(entry)




# In[192]:


f=open("Story.html","w+")
for entry in new:
    f.write(entry)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




