# 15.  
                        Clone a linked list with next and random pointer
##  Hard 
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">You are given a special&nbsp;linked list&nbsp;with&nbsp;<strong>N </strong>nodes where each node has a&nbsp;next pointer pointing to its&nbsp;next node. You are also given&nbsp;<strong>M</strong>&nbsp;random pointers , where you will be given <strong>M </strong>number of pairs denoting two nodes <strong>a</strong> and <strong>b</strong>&nbsp;&nbsp;<strong>i.e.&nbsp;</strong></span><span style="font-size:18px">a-&gt;arb = b<strong>.</strong></span></p>

<p><span style="font-size:18px"><img alt="ArbitLinked List1" class="aligncenter size-full wp-image-1254 img-responsive" src="https://contribute.geeksforgeeks.org/wp-content/uploads/clone.jpg" style="height:160px; width:450px" title="ArbitLinked List1"></span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 4, M = 2
value = {1,2,3,4}
pairs = {{1,2},{2,4}}
<strong>Output: </strong>1<strong>
Explanation: </strong>In this test case, there
re 4 nodes in linked list.&nbsp; Among these
4 nodes,&nbsp; 2 nodes have arbit pointer
set, rest two nodes have arbit pointer
as NULL. Second line tells us the value
of four nodes. The third line gives the
information about arbitrary pointers.
The first node arbit pointer is set to
node 2.&nbsp; The second node&nbsp;arbit pointer
is set to node 4.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 4, M = 2
value[] = {1,3,5,9}
pairs[] = {{1,1},{3,4}}
<strong>Output: </strong>1<strong>
Explanation: </strong>In the given testcase ,
applying the method as stated in the
above example, the output will be 1.</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
The task is to complete the function <strong>copyList</strong>() which takes one argument the head of the linked list to be cloned and should <strong>return</strong> the head of the cloned linked list.<br>
<strong>NOTE : </strong>If their is any node whose arbitrary pointer is not given then its by default null.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity</strong> : O(n)<br>
<strong>Expected Auxilliary Space </strong>: O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 100<br>
1 &lt;= M&nbsp;&lt;= N<br>
1 &lt;= a, b &lt;= 100</span></p>
 <p></p>
            </div>