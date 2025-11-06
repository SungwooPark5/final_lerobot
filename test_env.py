import lerobot
import gymnasium as gym

print("LeRobot 라이브러리를 임포트했습니다.")

try:
    # 1. Hub에서 시뮬레이션 환경(맵)을 불러옵니다.
    #    이것이 공식적인 public API입니다.
    env = lerobot.make(
        "gym-hil/pusht-image-v0",  #
        # render_mode="human" # 시뮬레이션 창을 보려면 이 주석을 해제하세요.
    )

    print(f"성공: '{env.spec.id}' 환경을 불러왔습니다.")

    # 2. 환경이 잘 작동하는지 테스트합니다.
    observation, info = env.reset(seed=42)
    print("환경이 성공적으로 리셋되었습니다.")
    print("관찰 공간(Observation Space):", env.observation_space)
    print("행동 공간(Action Space):", env.action_space)

    # 3. 임의의 행동(action)으로 몇 스텝 실행해 봅니다.
    for _ in range(10):
        action = env.action_space.sample()  # 임의의 행동 선택
        obs, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            print("에피소드 종료. 다시 리셋합니다.")
            observation, info = env.reset()
            
    env.close()
    print("테스트 완료: 환경이 정상적으로 작동합니다!")

except Exception as e:
    print(f"오류 발생: {e}")
    print("MuJoCo 의존성이 올바르게 설치되었는지 확인하세요.")
    print("터미널에서 'uv pip install \"lerobot[mujoco]\"'를 실행해 보세요.")