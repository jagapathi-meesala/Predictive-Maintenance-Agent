from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_manifest_core_open_gap_010_fields():
    manifest = yaml.safe_load((ROOT / "agent.yaml").read_text())
    assert manifest["spec_version"] == "0.1.0"
    assert re.fullmatch(r"[a-z][a-z0-9-]*", manifest["name"])
    assert re.fullmatch(r"\d+\.\d+\.\d+", str(manifest["version"]))
    assert isinstance(manifest["description"], str) and manifest["description"]


def test_declared_skills_and_tools_are_real():
    manifest = yaml.safe_load((ROOT / "agent.yaml").read_text())

    for skill in manifest["skills"]:
        skill_file = ROOT / "skills" / skill / "SKILL.md"
        assert skill_file.exists(), f"Missing skill: {skill_file}"

    for tool in manifest["tools"]:
        implementation = ROOT / "tools" / f"{tool.replace('-', '_')}.py"
        definition = ROOT / "tools" / f"{tool}.yaml"

        assert implementation.exists(), f"Missing tool implementation: {implementation}"
        assert definition.exists(), f"Missing tool definition: {definition}"


def test_skill_frontmatter_is_valid():
    manifest = yaml.safe_load((ROOT / "agent.yaml").read_text())

    for skill in manifest["skills"]:
        skill_file = ROOT / "skills" / skill / "SKILL.md"
        text = skill_file.read_text()

        assert text.startswith("---\n")
        assert "\n---\n" in text

        frontmatter = text.split("---\n", 2)[1]
        metadata = yaml.safe_load(frontmatter)

        assert metadata["name"] == skill
        assert isinstance(metadata["description"], str)
        assert metadata["description"]


def test_no_known_unsupported_fields():
    manifest = yaml.safe_load((ROOT / "agent.yaml").read_text())

    for key in ["display_name", "entrypoint", "portability"]:
        assert key not in manifest
