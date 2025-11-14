lerobot-eval \
    --policy.path=lerobot/act_aloha_sim_transfer_cube_human \
    --env.type=aloha \
    --env.task=AlohaTransferCube-v0 \
    --eval.batch_size=50 \
    --eval.n_episodes=500 \
    --policy.use_amp=false \
    --policy.device=cuda