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
from pathlib import Path
from pydantic import BaseModel

import pymupdf, fitz


def pdf_to_jpg(pdf_path, output_folder, dpi=200):
    """
    将PDF文件导出为JPG图片，允许自定义输出精度（DPI）。

    :param pdf_path: PDF文件的路径
    :param output_folder: 输出JPG图片的文件夹路径
    :param dpi: 输出图片的DPI（每英寸点数），默认为200
    """
    # 打开PDF文件
    doc = fitz.open(pdf_path)

    # 遍历PDF的每一页
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # 加载页面
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72.0, dpi / 72.0), alpha=False)  # 获取页面图片，调整DPI

        # 构建输出文件名
        output_filename = f"{output_folder}/page_{page_num + 1:03d}.jpg"

        # 保存图片
        pix.save(output_filename)

        # 释放资源
        pix = None

    # 关闭PDF文件
    doc.close()


def export_page_to_jpg(pdf_path, output_path, dpi=200):
    # 打开 PDF 文件
    doc = fitz.open(pdf_path)

    # 设置图像的 DPI
    zoom_x = dpi / 96
    zoom_y = dpi / 96
    mat = fitz.Matrix(zoom_x, zoom_y)

    # 遍历 PDF 中的每一页
    for page in doc:
        # 获取当前页的像素图
        pix = page.get_pixmap(matrix=mat)

        # 保存为 JPG 图像，可以设置 JPEG 质量
        pix.save(output_path + f"page-{page.number}.jpg", "jpg", jpg_quality=95)

    # 关闭文档
    doc.close()


if __name__ == "__main__":
    tar = r"Z:\work\2024\其他\加章\韦露斯\署名-报告-水文分析室\新建文件夹\1-5-署名-台山市处置港澳惰性拆建物料项目(A、B、C、D、E)区防洪潮评价报告.pdf"

    pdf_to_jpg(tar, ".")
    export_page_to_jpg(tar, ".")
