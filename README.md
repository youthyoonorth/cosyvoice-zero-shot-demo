# CosyVoice Zero-Shot Demo

基于开源 **CosyVoice** 框架完成的零样本语音合成（Zero-Shot Voice Cloning）复现与简单工程封装项目。  
本项目在官方代码基础上，补充了单条推理脚本、批量生成脚本和基础实验记录，用于快速验证 zero-shot 语音合成链路，并沉淀可复现的实验结果。

---

## 1. 项目简介

本项目主要完成了以下内容：

- 跑通 CosyVoice-300M 的 **zero-shot voice cloning** 推理流程
- 封装单条推理脚本 `inference.py`
- 封装批量生成脚本 `batch_inference.py`
- 支持参考音频驱动的音色迁移
- 支持文本列表批量生成与结果自动保存
- 记录生成语音时长、推理耗时和基础实验结果

> 说明：本项目聚焦于 **推理链路复现、脚本封装和实验记录**，不包含从零训练模型或大规模训练优化。

---

## 2. 项目结构

```text
.
├── inference.py                # 单条 zero-shot 推理脚本
├── batch_inference.py          # 批量生成脚本
├── texts.txt                   # 批量生成输入文本
├── experiment_notes.md         # 实验记录
├── requirements.no_trt.txt     # 去除 TensorRT 后的依赖记录
├── pretrained_models/          # 模型文件（不上传）
├── outputs/                    # 单条推理输出（不上传）
├── batch_outputs/              # 批量推理输出（不上传）
└── asset/
    ├── zero_shot_prompt.wav
    └── zero_shot_prompt_3s.wav
3. 环境配置

推荐使用 Python 3.10。

3.1 创建环境
conda create -n cosyvoice -y python=3.10
conda activate cosyvoice
3.2 克隆仓库
git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
cd CosyVoice
git submodule update --init --recursive
3.3 安装依赖
pip install -r requirements.no_trt.txt

说明：为快速跑通主流程，这里使用了去除 TensorRT 相关依赖的版本。
对于本项目的 zero-shot 推理与基础实验，这已经足够。

4. 模型下载

使用 ModelScope 下载 CosyVoice-300M：

python - <<'PY'
from modelscope import snapshot_download
snapshot_download('iic/CosyVoice-300M', local_dir='pretrained_models/CosyVoice-300M')
PY
5. 单条推理
5.1 命令
python inference.py \
  --text "你好，这是我用 CosyVoice 生成的一段测试语音。" \
  --prompt_text "希望你以后能够做的比我还好呦。" \
  --prompt_wav "./asset/zero_shot_prompt.wav" \
  --output_wav "./outputs/test1.wav"
5.2 功能说明
--text：目标合成文本
--prompt_text：参考音频对应文本
--prompt_wav：参考音频路径
--output_wav：输出音频保存路径
6. 批量生成
6.1 准备文本文件

texts.txt 示例：

你好，这是第一条批量测试语音。
大家好，这是第二条批量测试语音，我正在验证 CosyVoice 的批量生成功能。
今天天气不错，希望这次实验能够顺利完成。
6.2 命令
python batch_inference.py \
  --prompt_text "希望你以后能够做的比我还好呦。" \
  --prompt_wav "./asset/zero_shot_prompt.wav" \
  --text_file "./texts.txt" \
  --output_dir "./batch_outputs"
6.3 输出结果

运行后会在 batch_outputs/ 目录下生成：

sample_1.wav
sample_2.wav
sample_3.wav

同时终端会打印每条样本的推理耗时。

7. 实验记录

目前已完成以下基础实验：

7.1 基础 zero-shot 推理
输出文件：./outputs/test1.wav
采样率：22050 Hz
输出时长：约 4.052 s
7.2 同一文本，不同 prompt 长度对比
原始 prompt 输出：./outputs/test2.wav
3 秒 prompt 输出：./outputs/test2_prompt3s.wav
两者输出时长接近，说明短 prompt 条件下仍可正常完成生成
7.3 批量生成测试
批量成功生成 3 条语音
单次生成耗时约：
2.442 s
4.395 s
2.737 s

更多记录见：experiment_notes.md

8. 我在这个项目中做了什么

相较于直接运行官方示例，本项目额外完成了以下工作：

封装了单条推理脚本 inference.py
封装了批量生成脚本 batch_inference.py
增加了文本列表批量推理能力
记录了输出语音时长、耗时和基础实验结果
对 prompt 长度变化进行了简单对比实验
9. 后续计划
增加更完整的实验记录与自动日志保存
补充 Gradio / Web Demo
进一步梳理 CosyVoice 的模型结构与训练流程
对生成自然度、音色相似度和推理延迟做更系统评估
10. 致谢

本项目基于开源 CosyVoice 框架完成，核心模型与大部分底层实现来自官方仓库。
本仓库重点展示个人在 推理复现、脚本封装和实验记录 方面的工作。