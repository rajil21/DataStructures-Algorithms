# 4. Queue using circular array
## Easy 
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Given <strong>size</strong> of a queue and <strong>Q</strong> query. The task is to perform operations according to the type of query. Queries can be of following types:</span></p>

<p><span style="font-size:18px"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </strong>1)<strong> 1 element</strong>: This means <strong>push </strong>the <strong>element </strong>into the queue (allowed only when queue is not full).<br>
<strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </strong>2)<strong> 2</strong>: This means <strong>pop </strong>the <strong>element </strong>at front from the queue (allowed only when queue is not empty).</span></p>

<p><span style="font-size:18px"><strong>Input:</strong><br>
First line of input contains size of queue and Q queries. Next Q lines contains queries of any of the two types as given above.</span></p>

<p><span style="font-size:18px"><strong>Output:</strong><br>
For each query, the task is to push and pop element and print "<strong>1</strong>" (without quotes) if operations succeeds, else print "<strong>-1</strong>" (without quotes).</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= size &lt;= 10<sup>4</sup><br>
1 &lt;= Q &lt;= 10<sup>3</sup></span></p>

<p><span style="font-size:18px"><strong>User Task:</strong><br>
The task is to complete the functions <strong>push</strong>() and <strong>pop</strong>() which does push and pop according to the queue.</span></p>

<p><span style="font-size:18px"><strong>Example:<br>
Input:</strong><br>
2<br>
4 6<br>
1 1<br>
1 1<br>
1 1<br>
1 1<br>
1 1<br>
2<br>
4 5<br>
2<br>
2<br>
1 1<br>
1 2<br>
1 3</span></p>

<p><span style="font-size:18px"><strong>Output:</strong><br>
1<br>
1<br>
1<br>
1<br>
-1<br>
1<br>
-1<br>
-1<br>
1<br>
1<br>
1</span></p>

<p><span style="font-size:18px"><strong>Explanation:</strong><br>
<strong>Testcase 1:</strong> Upto query number 4, queue is having space to push elements, so ouput is 1 till this query. After this, since queue is full and you want to push element, so output is -1.</span></p>

<p><span style="font-size:18px"><strong>Testcase 2:</strong> When queue is empty, and you want to pop out element, output is -1.</span><br>
&nbsp;</p>
 <p></p>
            </div>