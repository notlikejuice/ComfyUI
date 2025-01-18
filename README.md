## Usage Examples

### Example 1: Basic Image Generation
To generate an image using a simple prompt, you can use the following command:
```bash
python main.py --prompt "A beautiful sunset over the mountains"
```

### Example 2: Using Custom Models
To use a custom model, specify the model path:
```bash
python main.py --model_path "path/to/your/model.ckpt" --prompt "A futuristic cityscape"
```

### Example 3: Batch Processing
You can process multiple images in a batch by providing a list of prompts:
```bash
python main.py --prompts "A cat", "A dog", "A landscape"
```

### Example 4: Saving Outputs
To save the generated images to a specific directory, use:
```bash
python main.py --output_dir "output/images" --prompt "A fantasy landscape"
```

### Example 5: Advanced Options
For advanced options, you can adjust parameters like resolution and steps:
```bash
python main.py --prompt "A magical forest" --resolution 512x512 --steps 50
