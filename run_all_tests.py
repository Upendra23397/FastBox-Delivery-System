import json
from pathlib import Path
from delivery_system import simulate_delivery


def main():
    test_dir = Path('test_cases')
    output_dir = Path('test_reports')
    output_dir.mkdir(exist_ok=True)

    for input_file in sorted(test_dir.glob('test_case_*.json')):
        data = json.loads(input_file.read_text(encoding='utf-8'))
        report, _, _ = simulate_delivery(data)
        output_file = output_dir / f'{input_file.stem}_report.json'
        output_file.write_text(json.dumps(report, indent=4), encoding='utf-8')
        print(f'{input_file.name} -> {output_file.name}')


if __name__ == '__main__':
    main()
