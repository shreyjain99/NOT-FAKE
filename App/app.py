import pickle
import streamlit as st



 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(header,content,model): 
    
    
    
 



    final_prob,sentences_array,sentences_prob,top_10_searches = 0,['sentence' for x in range(5)],[0 for x in range(5)],['sample text' for x in range(10)]
    
        
    return final_prob,sentences_array,sentences_prob,top_10_searches
      
  

# this is the main function in which we define our webpage  
def main():       
    
    st.title('FAKE NEWS PREDICTOR')
      

    header = st.text_area('HEADING')
    content = st.text_area('CONTENT')
    model = st.selectbox('MODEL',("BERT SMALL (COVID)", "BERT SMALL (GENERAL)", "LSTM", "BIDIRECTIONAL LSTM"))
    
    #for taking image as input
    #st.image('./header.png')
   

    #create space of lines
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    
    # when 'Predict' is clicked
    if st.button("Predict", help="click to predict"): 
        
        #calling prediction function 
        final_prob, sentences_array, sentences_prob, top_10_searches = prediction(header,content,model)
        
        #create space of 2 lines
        st.text(" ")
        st.text(" ")
        
        
        #display output
        html1 = """ 
        <h2 style="color:aqua;text-align:center;text-decoration:underline double;">OUTPUT</h2> 
        """
        st.markdown(html1, unsafe_allow_html = True) 
        
        
        #probability of news being fake
        st.text(" ")
        st.text(" ")
        st.markdown('PROBABILITY OF BEING FAKE IS {}'.format(final_prob))
        
        
        #sentence wise distribution
        st.text(" ")
        st.text(" ")
        html2 = """ 
        <h3 style="color:aqua;"><u>SENTENCE WISE DISTRIBUTION</u></h3> 
        """   
        st.markdown(html2, unsafe_allow_html = True) 
        for i in range(0,len(sentences_array)):
            col = st.beta_columns(2)
            col[0].write(sentences_array[i])
            col[1].write(sentences_prob[i])
        
 
        #similar searches
        st.text(" ")
        st.text(" ")
    
        html3 = """ 
        <h3 style="color:aqua;"><u>TOP SIMILAR SEARCHES</u></h3> 
        """   
        st.markdown(html3, unsafe_allow_html = True) 
        for i in range(0, len(top_10_searches)):
            st.text(" ")
            column = st.beta_columns(2)
            column[0].write(f'{i+1}')
            column[1].write(top_10_searches[i])

     
    
if __name__=='__main__': 
    main()
