from client import MultilingualAvatarLipSyncVideoCompilerClient

def main():
    client = MultilingualAvatarLipSyncVideoCompilerClient()
    res = client.compile_avatar_talking_head_video('Quarterly revenue presentation for multinational stakeholders', ['EN', 'DE', 'PT', 'KO'])
    print('Video Job: ' + res['video_job_id'] + ' (' + res['rendered_video_resolution'] + ')')
    print('Languages: ' + ', '.join(res['translated_languages']) + ' | Lip-Sync Accuracy: ' + str(res['neural_lip_sync_accuracy_score_pct']) + '%')
    print('Playlist URL: ' + res['output_multilingual_m3u8_playlist'])

if __name__ == '__main__':
    main()
