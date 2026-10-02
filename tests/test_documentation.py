from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_required_docs_exist():
    for name in ['SOUL.md','README.md','AGENTS.md','DUTIES.md','RULES.md','EXPLAINABILITY.md']:
        assert (ROOT/name).is_file()

def test_explainability_headings_exact():
    text=(ROOT/'EXPLAINABILITY.md').read_text()
    assert text.count('## Inputs and Data Sources')==1
    assert text.count('## Decision and Reasoning')==1
    assert text.count('## Limits and Constraints')==1
    assert '## Inputs\n' not in text and '## Decision\n' not in text and '## Limits\n' not in text
