from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound

def detect_language(code):
    try:
        lexer = guess_lexer(code)
        return lexer.name
    except ClassNotFound:
        return "unknown"
    

def get_extension(code):
    language_extensions = {
        "Python": ".py",
        "Java": ".java",
        "JavaScript": ".js",
        "C": ".c",
        "C++": ".cpp",
        "C#": ".cs",
        "Ruby": ".rb",
        "PHP": ".php",
        "Go": ".go",
        "Swift": ".swift",
        "Kotlin": ".kt",
        "Rust": ".rs",
        "HTML": ".html",
        "CSS": ".css",
        "TypeScript": ".ts",
        "Shell Script": ".sh",
        "Perl": ".pl",
        "R": ".R",
        "Scala": ".scala",
        "Lua": ".lua",
        "Dart": ".dart",
        "Objective-C": ".m",
        "Elixir": ".ex",
        "Haskell": ".hs",
        "MATLAB": ".m",
        "Groovy": ".groovy",
        "Visual Basic": ".vb",
        "Assembly": ".asm",
    }
    
    # return language_extensions.get(detect_language(code), "unknown1")
    return '.plaintext'