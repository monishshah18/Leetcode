<h2>161. One Edit Distance</h2><h3>Medium</h3><hr><div><p>Given two strings <code>s</code>&nbsp;and <code>t</code>, return <code>true</code> if they are both one edit distance apart, otherwise return <code>false</code>.</p>

<p>A string <code>s</code> is said to be one distance apart from a string <code>t</code> if you can:</p>

<ul>
	<li>Insert <strong>exactly one</strong> character into <code>s</code>&nbsp;to get&nbsp;<code>t</code>.</li>
	<li>Delete <strong>exactly one</strong> character from&nbsp;<code>s</code>&nbsp;to get&nbsp;<code>t</code>.</li>
	<li>Replace <strong>exactly one</strong> character of&nbsp;<code>s</code>&nbsp;with <strong>a different character</strong> to get&nbsp;<code>t</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "ab", t = "acb"
<strong>Output:</strong> true
<strong>Explanation:</strong> We can insert 'c' into s&nbsp;to get&nbsp;t.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "", t = ""
<strong>Output:</strong> false
<strong>Explanation:</strong> We cannot get t from s by only one step.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "a", t = ""
<strong>Output:</strong> true
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> s = "", t = "A"
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= t.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lower-case letters, upper-case letters <strong>and/or</strong> digits.</li>
</ul>
</div>