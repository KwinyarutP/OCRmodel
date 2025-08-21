#load model and evaluate in file 
from paddleocr import PPStructureV3

pipeline = PPStructureV3(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False
)

output = pipeline.predict(input="../../data/Data Foundation List.pdf",)

# Visualize the results and save the JSON results
for res in output:
    res.print() 
    res.save_to_json(save_path="output") 
    res.save_to_markdown(save_path="output")           