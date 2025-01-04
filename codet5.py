from transformers import RobertaTokenizer, T5ForConditionalGeneration
import torch
import ast

class CodeBlockVisitor(ast.NodeVisitor):
    def __init__(self, source_code):
        self.source_code = source_code
        self.code_blocks = []

    def visit_FunctionDef(self, node):
        self.code_blocks.append(ast.get_source_segment(self.source_code, node))
        self.generic_visit(node)
    
    def visit_For(self, node):
        self.code_blocks.append(ast.get_source_segment(self.source_code, node))
        self.generic_visit(node)
        
    def visit_While(self, node):
        self.code_blocks.append(ast.get_source_segment(self.source_code, node))
        self.generic_visit(node)
        
    def visit_If(self, node):
        self.code_blocks.append(ast.get_source_segment(self.source_code, node))
        self.generic_visit(node)

class CodeT5:
    def __init__(self):        
        if torch.backends.mps.is_available():
            # OVERRIDE FOR FASTER DEV
            self.device = torch.device('cpu')
            print('[INFO] Using CPU')
            
            '''
            device = torch.device('mps')
            print('[INFO] Using MPS')
            '''
        else:
            self.device = torch.device('cpu')
            print('[INFO] Using CPU')
            
        self.tokenizer = RobertaTokenizer.from_pretrained('Salesforce/codet5-base-multi-sum')
        self.model = T5ForConditionalGeneration.from_pretrained('Salesforce/codet5-base-multi-sum').to(self.device)
            
    def summarize_code(self, source_code):
        input_ids = self.tokenizer(source_code, return_tensors='pt').input_ids.to(self.device)
        generated_ids = self.model.generate(input_ids, max_length=100)
        summary = self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        return summary
    
    def extract_code_blocks(self, source_code):
        tree = ast.parse(source_code)
        visitor = CodeBlockVisitor(source_code)
        visitor.visit(tree)
        
        return visitor.code_blocks
    
    def summarize_by_line(self, code):
        code_lines = code.splitlines()
        output = []
        
        for line in code_lines:
            if line.strip():
                summary = self.summarize_code(line)
                print(f'Code: {line}\nSummary: {summary}\n')
                output.append(f'Summary: {summary}\n')
                
        return '\n'.join(output)
    
    def summarize_by_chunks(self, code):
        code_blocks = self.extract_code_blocks(code)
        output = []
        
        for block in code_blocks:
            summary = self.summarize_code(block)
            print(f'Code: {block}\nSummary: {summary}\n')
            output.append(f'{summary}\n')
            
        return '\n'.join(output)