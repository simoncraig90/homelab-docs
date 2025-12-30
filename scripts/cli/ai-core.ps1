$AI_CORE_URL = "http://192.168.0.147:11434/api/generate"
$Model = "qwen2.5:14b-instruct"

$Prompt = $args -join " "

if (-not $Prompt) {
    Write-Host 'Usage: .\ai-core.ps1 "your prompt here"' -ForegroundColor Yellow
    exit 1
}

$bodyObject = @{
    model  = $Model
    prompt = $Prompt
    stream = $false
}

$bodyJson = $bodyObject | ConvertTo-Json -Depth 4

try {
    $response = Invoke-RestMethod -Uri $AI_CORE_URL `
                                  -Method Post `
                                  -ContentType "application/json" `
                                  -Body $bodyJson

    if ($null -ne $response -and $response.response) {
        $response.response
    }
    else {
        Write-Error "AI-Core responded but no 'response' field was found in the payload."
    }
}
catch {
    Write-Error "Failed to contact AI-Core at $AI_CORE_URL"
    Write-Error $_.Exception.Message
    exit 1
}
