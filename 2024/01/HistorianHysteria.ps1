$lines = Get-Content "input"

$left = New-Object System.Collections.Generic.List[int]
$right = New-Object System.Collections.Generic.List[int]

foreach ($line in $lines) {
    $a, $b = $line.Split("   ")
    $left.Add([int]$a)
    $right.Add([int]$b)
}

$left = $left | Sort-Object
$right = $right | Sort-Object

function Solve-Part1 {
    $distance = 0
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $distance += [Math]::Abs($left[$i] - $right[$i])
    }
    return $distance
}

function Solve-Part2 {
    $similarityScore = 0
    $occurences = $right | Group-Object -AsHashTable
    foreach ($value in $left) {
        $similarityScore += $value * $occurences[$value].Count
    }
    return $similarityScore
}

"Part 1: $(Solve-Part1)" 
"Part 2: $(Solve-Part2)" 
