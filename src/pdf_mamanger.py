from pypdf import PdfWriter
import pathlib


def merge_pdfs(pdf_list, output_pdf: str = None):
    merger = PdfWriter()

    for pdf in pdf_list:
        merger.append(pdf)

    if output_pdf is None:
        pdf_file = pathlib.Path(pdf_list[0])
        output_pdf = str(pdf_file.resolve()).replace(pdf_file.suffix, "_merge.pdf")

    merger.write(output_pdf)
    merger.close()


if __name__ == "__main__":
    pdf_list = [
        r"Z:\work\2024\其他\加章\工作实绩-林芯伊、刘珊霞、周舜轩整理(1)\封面人员页-P章\2022年博罗水文站旱警水位-1.pdf",
        r"Z:\work\2024\其他\加章\工作实绩-林芯伊、刘珊霞、周舜轩整理(1)\封面人员页-P章\2022年博罗水文站旱警水位-2.pdf",
    ]

    merge_pdfs(pdf_list, r"Z:\work\2024\其他\加章\工作实绩-林芯伊、刘珊霞、周舜轩整理(1)\output.pdf")
