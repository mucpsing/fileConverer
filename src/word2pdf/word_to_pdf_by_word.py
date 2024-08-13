# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2024-08-09 17:33:05.566986
# @file_path "W:\CPS\MyProject\projsect_persional\python-file-scripts\src\word2pdf"
# @Filename "word_to_pdf_by_word.py"
# @Description: 调用系统安装的word进行pdf的转换
#
import os, sys, pathlib

sys.path.append("..")

from pydantic import BaseModel
from win32com import client
from pydantic import BaseModel, Field

from typing import List, Union


class WORD_CODE:  # 记录所有word代码
    pdf: int = 17


class CpsWordConverterConfig(BaseModel):
    overwrite: bool = Field(False, description="如果文件已存在，是否覆盖输出")
    show_details: bool = Field(False, description="是否打印错误")


class CpsWordConverter:
    def __init__(self, config: CpsWordConverterConfig = None):
        """
        @Description {description}

        - param config=None :{CpsWordConverterConfig} 实例配置

        @example
        ```python
        target = r"Z:/xxxdir/xxxx.docx"
        target_dir = r"Z:/work/2023/改图/2023职称/周末bk"

        # 初始化
        Config = CpsWordConverterConfig(overwrite=False, show_details=True)
        Convert = CpsWordConverter(Config)

        # 单独转换文件
        Convert.convert(target)

        # 遍历目录
        Convert.convert(target_dir)
        ```

        """
        # 检查当前系统环境是否安装了word
        if not self.__check():
            raise "实例化失败"

        if config:
            self.config = config
        else:
            self.config = CpsWordConverterConfig()

        self.word = None  # 存储word实例

    def print(self, *argvs, **keys):
        if self.config.show_details:
            print(*argvs, **keys)

    def convert(self, target: str) -> List[str]:
        """
        @Description 转换主函数

        - param target :{str} target可以是目录，也可以是文件，如果是目录，将直接进行递归

        """
        try:
            if not os.path.exists(target):
                self.print("目标不存在: ", target)
                return []

            # 判断是目录还是文件
            p = pathlib.Path(target)
            result = []
            if p.is_file():
                result.append(self.__word2pdf(p))
            elif p.is_dir():
                result = self.__dir_handler(p)

            return result
        except Exception as e:
            self.print("convert err: ", e)
            return []

    def __del__(self):
        if self.word:
            self.word.Quit()
            self.word = None

    def __check(self) -> bool:
        return True

    def __open_word(self):
        self.word = client.Dispatch("Word.Application")
        self.word.Visible = False

        return self.word

    def __dir_handler(self, dir_path: Union[str, pathlib.Path]) -> str:
        docx = list(pathlib.Path(dir_path).glob("**/*.docx"))
        doc = list(pathlib.Path(dir_path).glob("**/*.doc"))

        word_list = docx + doc

        result = []
        if len(word_list) == 0:
            return ""
        else:
            self.print("当前需要处理的文件有: ", len(word_list))

        for each in word_list:
            result.append(self.__word2pdf(each))

        return result

    @staticmethod
    def word_accept_all_revisions(word):
        """
        @Description 对当前的word文件进行一次接收所有修订操作，并原地保存

        - param word :{param} word实例

        """
        try:
            word.ActiveDocument.TrackRevisions = False
            # word.WordBasic.AcceptAllChangesInDoc() # 会报错，但也可以接收所有修订
            word.ActiveDocument.Revisions.AcceptAll()

            if word.ActiveDocument.Comments.Count >= 1:
                word.ActiveDocument.DeleteAllComments()

            return word
        except Exception as err:
            print("word_accept_all_revisions: ", err)
            return word

    def __word2pdf(self, word_file: pathlib.Path) -> str:
        """
        - param word_file :{str} `.doc|.docx`结尾的文件
        """
        try:
            # 获取同名的pdf输出路径
            word_file_path = str(word_file.resolve())
            output_pdf_path = str(word_file.resolve()).replace(word_file.suffix, ".pdf")

            # 已存在pdf，是否进行覆盖
            if os.path.exists(output_pdf_path):
                # 不覆盖的话，直接跳过
                if not self.config.overwrite:
                    output_pdf_path = output_pdf_path = str(word_file.resolve()).replace(word_file.suffix, "_1.pdf")
                    self.print("文件已存在，更改输出为: ", output_pdf_path)

            # 打开word应用程序
            if not self.word:
                self.word = self.__open_word()

            # 打开word文件
            doc = self.word.Documents.Open(word_file_path)

            # 所有修订
            self.word_accept_all_revisions(self.word)

            # 另存为后缀为".pdf"的文件，其中参数17表示为pdf
            doc.Activate()
            doc.SaveAs(output_pdf_path, WORD_CODE.pdf)

            # 关闭原来word文件
            doc.Close()

            self.print("完成转换: ", word_file)
            return output_pdf_path

        except Exception as e:
            self.print("word2pdf err: ", e)

            return ""


def example():
    target = r"Z:\work\2024\项目\东莞海腾码头补办水利手续\0808珠江水文水资源勘测中心-东莞海腾码头补办水利手续工作大纲及报价书(1).docx"
    target_dir = r"Z:\work\2023\改图\2023职称\周末bk"

    Config = CpsWordConverterConfig(overwrite=False, show_details=True)
    Convert = CpsWordConverter(Config)
    Convert.convert(target)


def main(target: str):
    Config = CpsWordConverterConfig(overwrite=False, show_details=True)
    Convert = CpsWordConverter(Config)
    Convert.convert(target)


if __name__ == "__main__":
    # example()
    import argparse, time

    # 初始化实例
    parser = argparse.ArgumentParser()

    # 解释参数
    parser.add_argument(
        "target",  # 不要处理的word文件
        help="可以是目录，也可以是.doc/.docx文件",
        type=str,
    )

    args = parser.parse_args()

    main(args.target)
