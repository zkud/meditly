#!/usr/bin/env python3

import time
import sys
import argparse
from typing import NoReturn
import asyncio

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='A simple CLI meditation timer with breathing guidance'
    )
    parser.add_argument(
        '-t', '--time',
        type=int,
        default=10,
        help='Meditation duration in minutes (default: 10)'
    )
    parser.add_argument(
        '-i', '--inhale',
        type=int,
        default=4,
        help='Inhale duration in seconds (default: 4)'
    )
    parser.add_argument(
        '-e', '--exhale',
        type=int,
        default=6,
        help='Exhale duration in seconds (default: 6)'
    )
    return parser

async def animate_breath(message: str, duration: int) -> None:
    """Animate breathing instruction with a simple progress indicator."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(duration):
        for frame in frames:
            sys.stdout.write(f'\r{frame} {message} ')
            sys.stdout.flush()
            await asyncio.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(message) + 2) + '\r')
    sys.stdout.flush()

async def meditation_session(duration: int, inhale: int, exhale: int) -> None:
    """Run a meditation session with the specified parameters."""
    end_time = time.time() + (duration * 60)
    
    try:
        print(f"Starting {duration} minute meditation session...")
        print("Press Ctrl+C to end the session")
        
        while time.time() < end_time:
            await animate_breath("Breathe in...", inhale)
            await animate_breath("Breathe out...", exhale)
            
        print("\nMeditation session completed. 🧘")
        
    except KeyboardInterrupt:
        print("\nMeditation session ended early. 🙏")
        sys.exit(0)

def main() -> NoReturn:
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        asyncio.run(meditation_session(args.time, args.inhale, args.exhale))
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
