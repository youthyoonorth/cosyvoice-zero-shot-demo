import os
import sys
import argparse
import torchaudio

sys.path.append('third_party/Matcha-TTS')
from cosyvoice.cli.cosyvoice import AutoModel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_dir', type=str, default='pretrained_models/CosyVoice-300M')
    parser.add_argument('--text', type=str, required=True, help='要合成的目标文本')
    parser.add_argument('--prompt_text', type=str, required=True, help='参考音频对应的文本')
    parser.add_argument('--prompt_wav', type=str, required=True, help='参考音频路径')
    parser.add_argument('--output_wav', type=str, default='outputs/result.wav')
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output_wav), exist_ok=True)

    cosyvoice = AutoModel(model_dir=args.model_dir)

    for i, j in enumerate(
        cosyvoice.inference_zero_shot(
            args.text,
            args.prompt_text,
            args.prompt_wav
        )
    ):
        torchaudio.save(args.output_wav, j['tts_speech'], cosyvoice.sample_rate)
        print(f'saved: {args.output_wav}')
        print(f'sample_rate: {cosyvoice.sample_rate}')
        break


if __name__ == '__main__':
    main()
