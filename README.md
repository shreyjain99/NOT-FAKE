<h2 align= "center"><em>NOT FAKE</em></h2>

<div align="center">
  <img height="400" src="https://github.com/shreyjain99/Not-Fake/blob/main/src%20files/coverimg.png"/>
</div>

<hr width="100%" size="2">

<h3 align= "left"> <b> Key Project Formulation </b> </h3>

<br>

<p>
<strong>Real World/Business Objective :</strong> Given any Text based news/ news article predict if the news is real or fake.
</p>

<br>

<p>
<strong>Motivation for the project :</strong> Fake news detection is crucial in today's digital age due to the rapid spread of misinformation across social media and online platforms. This misinformation can distort public perception, influence opinions, and have harmful societal consequences, especially during crises like elections or pandemics. Automated systems using machine learning and natural language processing are essential for quickly identifying and filtering fake news, as manual fact-checking cannot keep up with the scale of online content. These systems help protect the public from manipulation and maintain the integrity of the information ecosystem.
</p>

<br>

<p>
<strong>Constraints :</strong>
</p>
<ol>
<li>Probabilistic output</li>
<li>Interpretability is very important</li>
<li>No low-latency requirement</li>
</ol>

<br>

<p>
<strong>Get the data from :</strong> The data is gathered from various online open source websites.
</p>

<br>

<p>
<strong>ML Problem Formulation :</strong>
</p>
<p> <strong>Fake news text prediction (Recurrent Neural Networks) (Classification)</strong> </p>
<p> 
This project focused on building a powerful false news detection system using BERT-based transformer models and natural language processing techniques. Multiple datasets were merged, and both deep learning and machine learning models were implemented. Attention-based models were fine-tuned using transfer learning to capture complex patterns in the text. The solution integrates advanced techniques for efficient and accurate classification.
</p>

<br>
<br>

<p>
<strong>Performance metrics :</strong>
</p>
<ol>
<li>Accuracy</li>
<li>Confusion matrix</li>
</ol>

<hr width="100%" size="2">

<body>

  <h2>Project Summary</h2>

  <p>This project focuses on detecting false news articles using a Deep Learning system built on the BERT small architecture, along with natural language processing techniques. The system was developed through multiple stages, including the merging of several datasets to enhance model performance:</p>

  <h3>1. Merging Datasets and Data Preprocessing</h3>
  <p>Multiple datasets containing news articles and related information were merged to create a comprehensive dataset. This was followed by data cleaning and preparation, where irrelevant columns were dropped, missing values were handled, and text was processed for analysis. The preprocessing ensured that the dataset was structured for both traditional machine learning and deep learning models.</p>

  <h3>2. Data Splitting</h3>
  <p>After preprocessing, the data was split into training, validation, and testing sets. This ensured the model would be evaluated on unseen data, providing robust performance measures. Maintaining a balanced dataset was crucial for binary classification (true vs. false news).</p>

  <h3>3. Modeling</h3>
    <p><strong>Machine Learning Models:</strong> Naive Bayes and Passive Aggressive Classifier, known for their effectiveness in text classification tasks, were employed as baseline models. These were used to benchmark performance against more advanced models.</p>
    <p><strong>LSTM Models:</strong> Initially used to capture sequential patterns in the text. However, LSTM models were later found to be less efficient compared to transformer-based approaches.</p>
    <p><strong>Transformer Models:</strong> The BERT small architecture, an attention-based model, was implemented, leveraging transfer learning for fine-tuning. Transformers use self-attention mechanisms to capture relationships between words in a sentence, allowing the model to focus on important parts of the text. This approach resulted in a 12% accuracy improvement over previous models. Transfer learning also significantly reduced training time and lowered latency by 5%.</p>

  <h3>4. Performance Optimization</h3>
    <p>By leveraging transfer learning and fine-tuning the BERT model, the system achieved improved accuracy and efficiency. The final model delivered faster predictions, making it suitable for real-time detection of false news articles.</p>

   <p>This project successfully integrated multiple datasets, baseline machine learning models, deep learning, and attention-based transformer techniques to build a robust false news detection system.</p>

</body>

<hr width="100%" size="2">

<h2>Future Scope and Limitations</h2>
<ol>
<li>The datasets used in this project were very small due to lack of resources therefore huge datasets should be used.</li>
<li>More complex and layers of encoders and decoders can be added to BERT model as well as different attention based models can also be used to make more robust system.</li>
<li>Many different models and several web check and fact check systems can also be used along with machine learning and deep learning systems to tackle the problem.</li>
</ol>


<hr width="100%" size="2">
<br>

<p>
<strong>Skills and Software Tools Used in the Project :</strong>
</p>
<ul>
    <li>Data Analysis</li>
    <li>Natural Language Processing (NLP)</li>
    <li>Text Preprocessing</li>
    <li>Machine Learning Models</li>
    <li>Deep Learning Models</li>
    <li>Transformer Models (BERT)</li>
    <li>Recurrent Neural Networks (RNNs)</li>
    <li>Transfer Learning</li>
    <li>Python</li>
    <li>Pandas</li>
    <li>NumPy</li>
    <li>Scikit-learn</li>
    <li>TensorFlow/PyTorch</li>
</ul>

<hr width="100%" size="2">
