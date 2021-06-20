<h2>1904. The Number of Full Rounds You Have Played</h2><h3>Medium</h3><hr><div><p>A new online video game has been released, and in this video game, there are <strong>15-minute</strong> rounds scheduled every <strong>quarter-hour</strong> period. This means that at <code>HH:00</code>, <code>HH:15</code>, <code>HH:30</code> and <code>HH:45</code>, a new round starts, where <code>HH</code> represents an integer number from <code>00</code> to <code>23</code>. A <strong>24-hour clock</strong> is used, so the earliest time in the day is <code>00:00</code> and the latest is <code>23:59</code>.</p>

<p>Given two strings <code>startTime</code> and <code>finishTime</code> in the format <code>"HH:MM"</code> representing the exact time you <strong>started</strong> and <strong>finished</strong> playing the game, respectively, calculate the <strong>number of full rounds</strong> that you played during your game session.</p>

<ul>
	<li>For example, if <code>startTime = "05:20"</code> and <code>finishTime = "05:59"</code> this means you played only one full round from <code>05:30</code> to <code>05:45</code>. You did not play the full round from <code>05:15</code> to <code>05:30</code> because you started after the round began, and you did not play the full round from <code>05:45</code> to <code>06:00</code> because you stopped before the round ended.</li>
</ul>

<p>If <code>finishTime</code> is <strong>earlier</strong> than <code>startTime</code>, this means you have played overnight (from <code>startTime</code> to the midnight and from midnight to <code>finishTime</code>).</p>

<p>Return <em>the <strong>number of full rounds</strong> that you have played if you had started playing at </em><code>startTime</code><em> and finished at </em><code>finishTime</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> startTime = "12:01", finishTime = "12:44"
<strong>Output:</strong> 1
<strong>Explanation:</strong> You played one full round from 12:15 to 12:30.
You did not play the full round from 12:00 to 12:15 because you started playing at 12:01 after it began.
You did not play the full round from 12:30 to 12:45 because you stopped playing at 12:44 before it ended.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> startTime = "20:00", finishTime = "06:00"
<strong>Output:</strong> 40
<strong>Explanation:</strong> You played 16 full rounds from 20:00 to 00:00 and 24 full rounds from 00:00 to 06:00.
16 + 24 = 40.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> startTime = "00:00", finishTime = "23:59"
<strong>Output:</strong> 95
<strong>Explanation:</strong> You played 4 full rounds each hour except for the last hour where you played 3 full rounds.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>startTime</code> and <code>finishTime</code> are in the format <code>HH:MM</code>.</li>
	<li><code>00 &lt;= HH &lt;= 23</code></li>
	<li><code>00 &lt;= MM &lt;= 59</code></li>
	<li><code>startTime</code> and <code>finishTime</code> are not equal.</li>
</ul>
</div>