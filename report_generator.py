def generate_report(risks, file_path):
    with open(file_path, 'w') as f:
        f.write("Risk Report\n")
        f.write("="*30 + "\n")

        for risk in risks:
            f.write(risk + "\n")
