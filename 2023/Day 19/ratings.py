"""
As you reach the bottom of the relentless avalanche of machine parts, you discover that they're already forming a 
formidable heap. Don't worry, though - a group of Elves is already here organizing the parts, and they have a system.

To start, each part is rated in each of four categories:

x: Extremely cool looking
m: Musical (it makes a noise when you hit it)
a: Aerodynamic
s: Shiny
Then, each part is sent through a series of workflows that will ultimately accept or reject the part. 
Each workflow has a name and contains a list of rules; each rule specifies a condition and where to send the part 
if the condition is true. The first rule that matches the part being considered is applied immediately, and the part 
moves on to the destination described by the rule. (The last rule in each workflow has no condition and always applies 
if reached.)

Consider the workflow ex{x>10:one,m<20:two,a>30:R,A}. This workflow is named ex and contains four rules. 
If workflow ex were considering a specific part, it would perform the following steps in order:

Rule "x>10:one": If the part's x is more than 10, send the part to the workflow named one.
Rule "m<20:two": Otherwise, if the part's m is less than 20, send the part to the workflow named two.
Rule "a>30:R": Otherwise, if the part's a is more than 30, the part is immediately rejected (R).
Rule "A": Otherwise, because no other rules matched the part, the part is immediately accepted (A).
If a part is sent to another workflow, it immediately switches to the start of that workflow instead and never returns. 
If a part is accepted (sent to A) or rejected (sent to R), the part immediately stops any further processing.

The system works, but it's not keeping up with the torrent of weird metal shapes. The Elves ask if you can help sort a 
few parts and give you the list of workflows and some part ratings (your puzzle input). For example:

px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
The workflows are listed first, followed by a blank line, then the ratings of the parts the Elves would like you to sort. 
All parts begin in the workflow named in. In this example, the five listed parts go through the following workflows:

{x=787,m=2655,a=1222,s=2876}: in -> qqz -> qs -> lnx -> A
{x=1679,m=44,a=2067,s=496}: in -> px -> rfg -> gd -> R
{x=2036,m=264,a=79,s=2244}: in -> qqz -> hdj -> pv -> A
{x=2461,m=1339,a=466,s=291}: in -> px -> qkq -> crn -> R
{x=2127,m=1623,a=2188,s=1013}: in -> px -> rfg -> A
Ultimately, three parts are accepted. Adding up the x, m, a, and s rating for each of the accepted parts gives 7540 
for the part with x=787, 4623 for the part with x=2036, and 6951 for the part with x=2127. Adding all of the ratings 
for all of the accepted parts gives the sum total of 19114.

Sort through all of the parts you've been given; what do you get if you add together all of the rating numbers 
for all of the parts that ultimately get accepted?

reference: https://www.reddit.com/r/adventofcode/comments/18ltr8m/comment/ke010be/
saw some solutions with cool, kind of slow, and very brain consuming golf
"""
import re
ll = [x for x in open('ratings_input.txt').read().strip().split('\n\n')]
workflow, parts = ll

def ints(s):
	return list(map(int, re.findall(r'\d+', s)))

parts = [ints(l) for l in parts.split("\n")]
workflow = {l.split("{")[0]: l.split("{")[1][:-1] for l in workflow.split("\n")}

def eval2(part, work):
	w = workflow[work]
	x, m, a, s = part
	for it in w.split(","):
		if it == "R":
			return False
		if it == "A":
			return True
		if ":" not in it:
			return eval2(part, it)
		cond = it.split(":")[0]
		if eval(cond):
			if it.split(":")[1] == "R":
				return False
			if it.split(":")[1] == "A":
				return True
			return eval2(part, it.split(":")[1])
	raise Exception(w)

p1 = 0

for part in parts:
	if eval2(part, 'in'):
		p1 += sum(part)
print(p1)


def both(ch, gt, val, ranges):
	ch = 'xmas'.index(ch)
	ranges2 = []
	for rng in ranges:
		rng = list(rng)
		lo, hi = rng[ch]
		if gt:
			lo = max(lo, val + 1)
		else:
			hi = min(hi, val - 1)
		if lo > hi:
			continue
		rng[ch] = (lo, hi)
		ranges2.append(tuple(rng))
	return ranges2


def acceptance_ranges_outer(work):
	return acceptance_ranges_inner(workflow[work].split(","))

def acceptance_ranges_inner(w):
	it = w[0]
	if it == "R":
		return []
	if it == "A":
		return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
	if ":" not in it:
		return acceptance_ranges_outer(it)
	cond = it.split(":")[0]
	gt = ">" in cond
	ch = cond[0]
	val = int(cond[2:])
	val_inverted = val + 1 if gt else val - 1
	if_cond_is_true = both(ch, gt, val, acceptance_ranges_inner([it.split(":")[1]]))
	if_cond_is_false = both(ch, not gt, val_inverted, acceptance_ranges_inner(w[1:]))
	return if_cond_is_true + if_cond_is_false

p2 = 0
for rng in acceptance_ranges_outer('in'):
	v = 1
	for lo, hi in rng:
		v *= hi - lo + 1
	p2 += v
print(p2)