# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2024-08-09 17:59:33.825123
# @file_path "W:\CPS\MyProject\projsect_persional\python-file-scripts\src\pdf2img"
# @Filename "mupdf.py"
# @Description: 功能描述
#
import os, sys

sys.path.append("..")

from os import path

import fitz
from PIL import Image
import io
from pypdf import PdfWriter
import pathlib


def merge_pdfs(pdf_list, output_pdf: str = None):
    # 创建一个新的 PDF 文档对象
    merged_doc = fitz.open()

    # 遍历所有输入的 PDF 文件
    for pdf in pdf_list:
        # 打开当前 PDF 文件
        src_doc = fitz.open(pdf)
        # 将当前 PDF 的所有页面插入到合并文档
        merged_doc.insert_pdf(src_doc)
        # 关闭源文档
        src_doc.close()

    # 处理默认输出路径
    if output_pdf is None:
        first_pdf = pathlib.Path(pdf_list[0])
        # 生成新文件名：原文件名 + "_merge.pdf"
        output_pdf = first_pdf.resolve().parent / (first_pdf.stem + "_merge.pdf")
        output_pdf = str(output_pdf)

    # 保存合并后的文档
    merged_doc.save(output_pdf)
    # 关闭合并文档
    merged_doc.close()


def export_pdf_to_paper_size(pdf_path, output_path, dpi=300, paper_size="A4"):
    # 定义A4和A3的尺寸（毫米）并转换为像素
    paper_sizes = {"A4": (210, 297), "A3": (297, 420)}
    width_mm, height_mm = paper_sizes.get(paper_size, ("A4"))

    # 毫米转英寸再乘以DPI
    target_width = int(width_mm / 25.4 * dpi)
    target_height = int(height_mm / 25.4 * dpi)

    # 打开PDF并获取页面
    doc = fitz.open(pdf_path)
    for page in doc:
        original_width = page.rect.width  # 原始宽度（点）
        original_height = page.rect.height  # 原始高度（点）

        # 计算适应目标尺寸的缩放比例
        scale_w = target_width / original_width
        scale_h = target_height / original_height
        scale = min(scale_w, scale_h)  # 保持宽高比

        # 生成缩放后的图像
        matrix = fitz.Matrix(scale, scale)
        pix = page.get_pixmap(matrix=matrix, dpi=dpi)
        # pix.save(output_path + f"page-{page.number}.jpg", "jpg", jpg_quality=70)

        img = Image.open(io.BytesIO(pix.tobytes()))

        # 创建目标尺寸画布并居中粘贴
        canvas = Image.new("RGB", (target_width, target_height), (255, 255, 255))
        x = (target_width - img.width) // 2
        y = (target_height - img.height) // 2
        canvas.paste(img, (x, y))

        # 保存结果
        canvas.info["dpi"] = (dpi, dpi)  # 写入DPI信息
        canvas.save(output_path + f"page-{page.number}.jpg", "JPEG", quality=95, dpi=(dpi, dpi))

    doc.close()


if __name__ == "__main__":
    tar = path.abspath(r"../testData/广州市番禺区金光大道工程(富怡路至亚运大道以南段)防洪评价工作大纲及报价书.pdf")
    pdf_list = [
        path.abspath(r"../testData/1.pdf"),
        path.abspath(r"../testData/2.pdf"),
    ]

    # pdf_to_jpg(tar, ".")
    # export_pdf_to_paper_size(tar, ".")
    merge_pdfs(pdf_list, "./merge_pdf_test.pdf")
