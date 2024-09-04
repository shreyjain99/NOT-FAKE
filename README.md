<h2 align= "center"><em>NOT FAKE</em></h2>

<div align="center">
  <img height="400" src="https://github.com/shreyjain99/Not-Fake/blob/main/src%20files/coverimg.png"/>
</div>

<hr width="100%" size="2">

<h3 align= "left"> <b> Key Project Formulation </b> </h3>

<br>

<p>
<strong>Real World/Business Objective :</strong> Given a directed social graph, have to predict missing links to recommend users
</p>

<br>

<p>
<strong>Constraints :</strong>
</p>
<ol>
<li>Probability of prediction is useful to recommend ighest probability links</li>
<li>No low-latency requirement.</li>
</ol>

<br>

<p>
<strong>Get the data from :</strong> https://www.kaggle.com/c/FacebookRecruiting
<br>The data is from facebook recruiting prediction competition hosted on kaggle.
</p>

<br>

<p>
<strong>Data Collection :</strong>
<br>
</p>
<p>Taken data from facebook's recruting challenge on kaggle https://www.kaggle.com/c/FacebookRecruiting
data contains two columns source and destination eac edge in graph - Data columns (total 2 columns): source_node int64 and destination_node int64 </p>

<br>

<p>
<strong>ML Problem Formulation :</strong>
</p>
<p> <strong>Link Prediction in graph</strong> </p>
<p> 
Generated training samples of good and bad links from given directed graph and for each link got some features like no of followers, is he followed back, page rank, katz score, adar index, some svd fetures of adj matrix, some weight features etc. and trained ml model based on these features to predict link.
</p>

<br>
<br>

<p>
<strong>Performance metrics :</strong>
</p>
<ol>
<li>Both precision and recall is important so F1 score is good choice </li>
<li>Confusion matrix</li>
</ol>

<hr width="100%" size="2">

<h2>Summary</h2>

<p>In this project, the dataset provided consisted of directed graph data with approximately 1.86 million nodes and 9.43 million edges. The data, obtained from Kaggle's Facebook Recruiting competition, included only connected nodes, though the theoretical number of possible edges is in the order of 10<sup>12</sup>.</p>

<p>During exploratory data analysis (EDA), it was found that 90% of users had fewer than 12 followers, highlighting the dataset's sparsity. The dataset was highly imbalanced, containing only one classification label, so a random sample of negative examples (y = 0, where the link is not present) was created to balance the training and test datasets.</p>

<p>Feature engineering was a critical part of the project, where various types of features were extracted, including:</p>

<ul>
    <li><strong>Similarity Measures</strong> (e.g., Adar index)</li>
    <li><strong>Ranking Measures</strong> (e.g., PageRank, Katz Centrality, HITS Score)</li>
    <li><strong>Graph Features</strong> (e.g., Connected Components, Shortest Path)</li>
    <li><strong>Weight Features</strong></li>
    <li><strong>SVD Features</strong> using the adjacency matrix (with n_components = 6)</li>
</ul>

<p>Two models, Random Forest and XGBoost, were trained on the extracted features. While both models were used for the prediction task, XGBoost took the most time to run due to its complexity and the size of the dataset.</p>

<h3>Model Performance:</h3>

<table>
    <tr>
        <th>Model</th>
        <th>n_estimators</th>
        <th>max_depth</th>
        <th>Train f1-Score</th>
        <th>Test f1-Score</th>
    </tr>
    <tr>
        <td>Random Forest</td>
        <td>72</td>
        <td>14</td>
        <td>0.962</td>
        <td>0.926</td>
    </tr>
    <tr>
        <td>XGBoost</td>
        <td>76</td>
        <td>14</td>
        <td>0.996</td>
        <td>0.927</td>
    </tr>
</table>

<p>This case study showcases the importance of feature engineering in graph-based machine learning tasks, particularly when dealing with imbalanced datasets and large-scale data. The models performed well, with XGBoost achieving a slightly higher train f1-score but similar test f1-score compared to Random Forest.</p>

</body>


<hr width="100%" size="2">

<h2>Observations</h2>

<p>Understanding graph structures and feature engineering was crucial for this case study. The Random Forest model found <strong>"follows_back"</strong> as the most important feature, followed by <strong>"weight_f2"</strong> and <strong>"shortest_path."</strong> However, XGBoost delivered the best results, despite taking longer to train. In XGBoost, <strong>"follows_back"</strong> was also the top feature, followed by <strong>"cosine_follower"</strong> and <strong>"weight_f1."</strong> This highlights the importance of effective feature selection in graph-based machine learning tasks.</p>

<hr width="100%" size="2">
