function TwoSum {
    param (
        [int[]]$nums,
        [int]$target
    )

    $map = @{}

    for ($i = 0; $i -lt $nums.Length; $i++) {
        $complement = $target - $nums[$i]
        if ($map.ContainsKey($complement)) {
            return @($map[$complement], $i)
        }
        $map[$nums[$i]] = $i
    }

    return @()
}

# Example usage
$nums = @(2, 7, 11, 15)
$target = 9
$result = TwoSum -nums $nums -target $target
Write-Host ($result)