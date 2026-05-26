# -*- coding: utf-8 -*-
# 00_audio_placeholder.rpy
# 自动生成静默音频占位文件，方便开发时测试音效触发点
# 正式版替换真实音频后，占位文件不会被覆盖（已有文件会跳过）

init python:
    import os
    import struct

    def _generate_silent_wav(filepath, duration=1.0, sample_rate=44100):
        """生成静默 WAV 文件（如果尚不存在）"""
        if os.path.exists(filepath):
            return

        dirname = os.path.dirname(filepath)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)

        num_samples = int(sample_rate * duration)
        data_size = num_samples * 2  # 16-bit mono

        try:
            with open(filepath, 'wb') as f:
                # RIFF header
                f.write(b'RIFF')
                f.write(struct.pack('<I', 36 + data_size))
                f.write(b'WAVE')
                # fmt subchunk
                f.write(b'fmt ')
                f.write(struct.pack('<I', 16))       # subchunk size
                f.write(struct.pack('<H', 1))         # PCM format
                f.write(struct.pack('<H', 1))         # mono
                f.write(struct.pack('<I', sample_rate))
                f.write(struct.pack('<I', sample_rate * 2))
                f.write(struct.pack('<H', 2))         # block align
                f.write(struct.pack('<H', 16))        # bits per sample
                # data subchunk
                f.write(b'data')
                f.write(struct.pack('<I', data_size))
                f.write(b'\x00' * data_size)
        except Exception:
            pass  # 写入失败时静默跳过，不影响游戏启动

    def _make_audio_placeholders():
        gamedir = renpy.config.gamedir
        audio = os.path.join(gamedir, "audio")

        _generate_silent_wav(os.path.join(audio, "night_wind.wav"), duration=3.0)
        _generate_silent_wav(os.path.join(audio, "cat_meow.wav"), duration=1.0)
        _generate_silent_wav(os.path.join(audio, "brick_hit.wav"), duration=0.5)
        _generate_silent_wav(os.path.join(audio, "pencil_write.wav"), duration=1.5)

    if AUTO_AUDIO_PLACEHOLDER:
        _make_audio_placeholders()
