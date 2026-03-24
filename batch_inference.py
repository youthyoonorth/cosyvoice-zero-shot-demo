import os
import sys
import time
import argparse
import torchaudio

sys.path.append('third_party/Matcha-TTS')
from cosyvoice.cli.cosyvoice import AutoModel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_dir', type=str, default='pretrained_models/CosyVoice-300M')
    parser.add_argument('--prompt_text', type=str, required=True)
    parser.add_argument('--prompt_wav', type=str, required=True)
    parser.add_argument('--text_file', type=str, required=True)
    parser.add_argument('--output_dir', type=str, default='batch_outputs')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    cosyvoice = AutoModel(model_dir=args.model_dir)

    with open(args.text_file, 'r', encoding='utf-8') as f:
        texts = [line.strip() for line in f if line.strip()]

    for idx, text in enumerate(texts, 1):
        t0 = time.time()
        out_path = os.path.join(args.output_dir, f'sample_{idx}.wav')

        for j in cosyvoice.inference_zero_shot(
            text,
            args.prompt_text,
            args.prompt_wav
        ):
            torchaudio.save(out_path, j['tts_speech'], cosyvoice.sample_rate)
            break

        elapsed = time.time() - t0
        print(f'[{idx}] saved: {out_path} | elapsed_sec={elapsed:.3f} | text={text}')


if __name__ == '__main__':
    main()
