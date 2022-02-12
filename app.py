import streamlit as st
import os
import runpy
import streamlit.components.v1 as components
#st.set_page_config(layout="wide")


class stwidget:
  def __init__(self,kind,sidebar,name):
    self.kind = kind
    self.sidebar = sidebar
    if name:
      self.name = name
    else:
      self.name = None
  def get_code(self):
    if self.sidebar==True:
      code = f"st.sidebar.{self.kind}"#('{self.name}')"
    else:
      code = f"st.{self.kind}"#('{self.name}')"
    if self.name:
      code = code + f"('{self.name}')"
    else:
      code = code + "()"


    return code

st.set_page_config(page_title="Streamlit App", page_icon="🤖",layout="wide")

#st.title('Streamlit No Code app')

widgets = ['title','header','subheader','balloons','image','text','button','checkbox','slider','text_input','number_input','camera_input']


#if selection equal a number, then show that number
#code_list=[]
#two columns usint st.beta_columns
col1,col2 = st.columns([8,2])
select_widget=col2.selectbox('select',widgets)

#sel_url='https://share.streamlit.io/st-hack/st_nocode/main/app.py/Nocode/'#st.text_input('Enter url')
#with col1:
#  components.iframe(sel_url,height=600,scrolling=True)


if 'code_list' not in st.session_state:
    st.session_state.code_list = []


with col2.form('form'):
    is_sidebar = st.checkbox('sidebar')
    # ask for balloons with a checkbox


    label = st.text_input('label or text')
    wid = stwidget(select_widget,is_sidebar,label)   
    subm= st.form_submit_button('submit')
    if subm:        
        st.session_state.code_list.append(wid.get_code())

# ask for columns with a checkbox
#cols = st.beta_columns([6,2])
#ask_cols = col2.checkbox('columns')
#if ask_cols:
  #ask for the number of columns
#  cols = col2.number_input('columns',2,4)
#  if cols:
#    if cols==2:
#      st.session_state.code_list.append('col1,col2 = st.columns(2)')
#      st.session_state.code_list.append('col1.markdown("col1")')
#      st.session_state.code_list.append('col2.markdown("col2")')
#    elif cols==3:
#      st.session_state.code_list.append('col1,col2,col3 = st.columns(3)')
#      st.session_state.code_list.append('col1.markdown("col1")')
#      st.session_state.code_list.append('col2.markdown("col2")')
#      st.session_state.code_list.append('col3.markdown("col3")')

#    elif cols==4:
#      st.session_state.code_list.append('col1,col2,col3,col4 = st.columns(4)')
#      st.session_state.code_list.append('col1.markdown("col1")')
#      st.session_state.code_list.append('col2.markdown("col2")')
#      st.session_state.code_list.append('col3.markdown("col3")')
#      st.session_state.code_list.append('col4.markdown("col4")')

      





if 'st.balloons()' in st.session_state.code_list:
  #st.write('balloons')
  #ask if we want to remove the balloons with a checkbox
  remove_balloons = col2.checkbox('remove balloons')
  if remove_balloons:
    st.session_state.code_list.remove('st.balloons()')

#ask if we want to remove the last elemente in the list using a button
remove_last = col2.button('Undo')
if remove_last:
  st.session_state.code_list.pop()
#with col2:
#    code_lines = st.multiselect(
#     'your code',
#     st.session_state.code_list,
#     st.session_state.code_list)
#write code_list to a file with each line as a code snippet

if not os.path.exists('pages_'):
  os.makedirs('pages_')

with open('pages_/01_Nocode.py','w') as f:
    f.write('import streamlit as st\n')
    for code in st.session_state.code_list:
        f.write(code+'\n')      

with col1:
    runpy.run_path('pages_/01_Nocode.py')

code_string = '\n'.join(st.session_state.code_list)
#st.code(code_string)
with open('pages_/02_code.py','w') as f:
  f.write('import streamlit as st\n')
  f.write('with open("pages_/01_Nocode.py","r") as f:\n')
  f.write('  code = f.read()\n')
  f.write(f'st.code(code,language="python")')
