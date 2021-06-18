<h2>828. Count Unique Characters of All Substrings of a Given String</h2><h3>Hard</h3><hr><div><p>Let's define a function <code>countUniqueChars(s)</code>&nbsp;that returns the number of unique characters on <code>s</code>, for example if <code>s = "LEETCODE"</code>&nbsp;then <code>"L"</code>, <code>"T"</code>,<code>"C"</code>,<code>"O"</code>,<code>"D"</code> are the unique characters since they appear only once in <code>s</code>, therefore&nbsp;<code>countUniqueChars(s) = 5</code>.<br>
<br>
On this problem given a string <code>s</code> we need to return the sum of&nbsp;<code>countUniqueChars(t)</code>&nbsp;where <code>t</code> is a substring of <code>s</code>. Notice that some substrings can be repeated so on this case you have to count the repeated ones too.</p>

<p>Since the answer can be very large, return&nbsp;the answer&nbsp;modulo&nbsp;<code>10 ^ 9 + 7</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "ABC"
<strong>Output:</strong> 10
<strong>Explanation: </strong>All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "ABA"
<strong>Output:</strong> 8
<strong>Explanation: </strong>The same as example 1, except <code>countUniqueChars</code>("ABA") = 1.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "LEETCODE"
<strong>Output:</strong> 92
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 10^4</code></li>
	<li><code>s</code>&nbsp;contain upper-case English letters only.</li>
</ul>
</div>