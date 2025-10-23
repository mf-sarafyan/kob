# Ollama GPU and Memory Configuration

# Set GPU overhead (1GB = 1024000000 bytes)
$env:OLLAMA_GPU_OVERHEAD = "1024000000"

# Limit number of loaded models
$env:OLLAMA_MAX_LOADED_MODELS = "1"

# Set context length
$env:OLLAMA_CONTEXT_LENGTH = "2048"

# Disable NUMA optimization
$env:OLLAMA_SCHED_SPREAD = "0"

# Optional: Set maximum queue length
$env:OLLAMA_MAX_QUEUE = "1"

# Print out the set variables for verification
Write-Host "Ollama Environment Variables Set:"
Write-Host "OLLAMA_GPU_OVERHEAD: $env:OLLAMA_GPU_OVERHEAD"
Write-Host "OLLAMA_MAX_LOADED_MODELS: $env:OLLAMA_MAX_LOADED_MODELS"
Write-Host "OLLAMA_CONTEXT_LENGTH: $env:OLLAMA_CONTEXT_LENGTH"
Write-Host "OLLAMA_SCHED_SPREAD: $env:OLLAMA_SCHED_SPREAD"
Write-Host "OLLAMA_MAX_QUEUE: $env:OLLAMA_MAX_QUEUE"

# Optional: Restart Ollama service
# Uncomment if you want to restart the service after setting variables
# Restart-Service ollama
