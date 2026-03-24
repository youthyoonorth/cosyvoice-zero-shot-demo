# CosyVoice 零样本语音合成实验记录

## 环境
- 模型：CosyVoice-300M
- 采样率：22050 Hz
- 推理方式：zero-shot voice cloning

## 实验 1：基础推理
- 输出文件：./outputs/test1.wav
- 输出时长：4.052 s
- 备注：基础 zero-shot 推理成功

## 实验 2：同一文本，不同 prompt 长度
### 2.1 原始 prompt
- 输出文件：./outputs/test2.wav
- 输出时长：6.455 s

### 2.2 3 秒 prompt
- 输出文件：./outputs/test2_prompt3s.wav
- 输出时长：6.490 s
- RTF：0.6608

## 初步观察
- 3 秒 prompt 下仍能成功完成 zero-shot 语音生成
- 对同一文本，输出语音总时长与原始 prompt 版本接近
- 后续需要主观试听比较音色相似度、自然度和韵律差异
