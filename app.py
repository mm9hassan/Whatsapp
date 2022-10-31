import streamlit as st
import  helper
import matplotlib.pyplot as plt
import time



# file Uplod menu

file=st.sidebar.file_uploader('WhatsApps file','.txt')
# side bar menu
if file is not None:
    with st.spinner('Wait for it...'):
        time.sleep(1)


    uplo=file.getvalue().decode('utf-8')
    df=helper.pre(uplo)

    a=df['user'].unique().tolist()
    a.sort()
    a.insert(0,'Over All')

    user= st.sidebar.selectbox('Select Options',options=a)


    st.sidebar.title('Chat Analysis')



    if st.sidebar.button('show Analysis'):
        st.header('Anlysis ' +str(user))
        if user =='Over All':
            
            col1,=st.sidebar.columns(1)
            with col1:
                st.header('Export to CSV')
                st.sidebar.download_button('Download File',data=helper.covert_csv(df),file_name='WhatsApp Analysis.csv')
            
            


        else:
            # st.dataframe(df[df['user']==str(user)],use_container_width=True)
            single=helper.person_cloud(user,df)
            fig, ax = plt.subplots()
            plt.axis('off')
            ax.imshow(single)
            st.pyplot(fig,)
            
        
    

        col1,col2,col3,col4=    st.columns(4)
        with col1:
            st.header('Total Messages')
            st.title(helper.message_count(user,df))
        with  col2:
            st.header('Total Words')
            st.title(helper.word_count(user,df))
        with col3:
            st.header('Total Media')
            st.title(helper.message_count(user,df))
        with col4:
            st.header('Total Links')
            st.title(helper.media_count(user,df))
        
            
            
        
        

        
    # top person 
        if user =='Over All':
            a,b=helper.top_person(df)
            first=helper.message_top(df)

            col1,col2 = st.columns(2,gap='medium')

            with col1:
                st.header('Top messages persons')
                st.bar_chart(a,use_container_width=True)
            with col2:
                st.header('Contibustions')
                st.dataframe(b,use_container_width=True,height=385)
            st.title('WordCloud')
            word_all=helper.cloud(df)
            fig, ax = plt.subplots()
            ax.imshow(word_all)
            plt.axis('off')
            st.pyplot(fig)

            
            st.header('Top messages')
            st.dataframe(first,use_container_width=True)

        else:

        
            st.header('Top messages')
            st.dataframe(helper.message_top_u(user,df),use_container_width=True)

    
    


    
    
    
    
