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
BACKGROUND_COLOR = 'white'
COLOR = 'black'

def set_page_container_style(
        max_width: int = 2100, max_width_100_percent: bool = False,
        padding_top: int = 0, padding_right: int = 1, padding_left: int = 1, padding_bottom: int = 10,
        color: str = COLOR, background_color: str = BACKGROUND_COLOR,
    ):
        if max_width_100_percent:
            max_width_str = f'max-width: 100%;'
        else:
            max_width_str = f'max-width: {max_width}px;'
        st.markdown(
            f'''
            <style>
                .reportview-container .sidebar-content {{
                    padding-top: {padding_top}rem;
                }}
                .reportview-container .main .block-container {{
                    {max_width_str}
                    padding-top: {padding_top}rem;
                    padding-right: {padding_right}rem;
                    padding-left: {padding_left}rem;
                    padding-bottom: {padding_bottom}rem;
                }}
                .reportview-container .main {{
                    color: {color};
                    background-color: {background_color};
                }}
            </style>
            ''',
            unsafe_allow_html=True,
        )

set_page_container_style()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#st.title('Streamlit No Code app')

widgets = ['balloons','title','header','subheader','image','text','button','checkbox','slider','text_input','number_input','camera_input']


#if selection equal a number, then show that number
#code_list=[]
#two columns usint st.beta_columns
col1,col2 = st.columns([8,2])
select_widget=col2.selectbox('select',widgets)

sel_url='http://localhost:8501/Nocode/'#st.text_input('Enter url')
with col1:
  components.iframe(sel_url,height=600,scrolling=True)


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
ask_cols = col2.checkbox('columns')
if ask_cols:
  #ask for the number of columns
  cols = col2.number_input('columns',2,4)
  if cols:
    if cols==2:
      st.session_state.code_list.append('col1,col2 = st.columns(2)')
      st.session_state.code_list.append('col1.markdown("col1")')
      st.session_state.code_list.append('col2.markdown("col2")')
    elif cols==3:
      st.session_state.code_list.append('col1,col2,col3 = st.columns(3)')
      st.session_state.code_list.append('col1.markdown("col1")')
      st.session_state.code_list.append('col2.markdown("col2")')
      st.session_state.code_list.append('col3.markdown("col3")')

    elif cols==4:
      st.session_state.code_list.append('col1,col2,col3,col4 = st.columns(4)')
      st.session_state.code_list.append('col1.markdown("col1")')
      st.session_state.code_list.append('col2.markdown("col2")')
      st.session_state.code_list.append('col3.markdown("col3")')
      st.session_state.code_list.append('col4.markdown("col4")')

      





if 'st.balloons()' in st.session_state.code_list:
  #ask if we want to remove the balloons with a checkbox
  remove_balloons = col2.checkbox('remove balloons')
  if remove_balloons:
    st.session_state.code_list.remove('st.balloons()')

#with col2:
#    code_lines = st.multiselect(
#     'your code',
#     st.session_state.code_list,
#     st.session_state.code_list)
#write code_list to a file with each line as a code snippet
with open('pages/01_Nocode.py','w') as f:
    f.write('import streamlit as st\n')
    for code in st.session_state.code_list:
        f.write(code+'\n')      

code_string = '\n'.join(st.session_state.code_list)
#st.code(code_string)
with open('pages/02_code.py','w') as f:
  f.write('import streamlit as st\n')
  f.write('with open("pages/01_Nocode.py","r") as f:\n')
  f.write('  code = f.read()\n')
  f.write(f'st.code(code,language="python")')
    #for code in st.session_state.code_list:
    #    f.write(code+'\n')  
#with col1:
#    runpy.run_path('code.py')



