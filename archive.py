import argparse
import os
from datetime import datetime, timedelta, timezone
import logging

from radiko.recorder import record_time_free


def _get_args():
    parser = argparse.ArgumentParser(description='record radiko')
    parser.add_argument('station', type=str, help='radiko station')
    parser.add_argument('start', type=int, help='start time')
    parser.add_argument('end', type=int, help='end time')
    parser.add_argument('program', type=str, help='radiko program name')
    parser.add_argument('timeout',
                        type=float,
                        default=None,
                        nargs='?',
                        help='limit time of recording.(unit:miniutes)')
    args = parser.parse_args()
    return args.station, args.start, args.end, args.program, args.timeout


if __name__ == "__main__":
    logging.basicConfig(filename=os.getenv('RADIKO_RECORDER_LOG_FILE',
                                           f'/var/log/record_radiko.log'),
                        level=logging.DEBUG)
    station, start, end, program, timeout = _get_args()

    JST = timezone(timedelta(hours=+9), 'JST')
    current_time = datetime.now(tz=JST).strftime("%Y%m%d%H%M%S")
    logging.debug(f'current time: {current_time}, '
                  f'station: {station}, '
                  f'program name: {program}, '
                  f'start: {start}, '
                  f'end: {end}')
    out_file_name = f'./output/{start}_{station}_{program}.m4a'
    logging.debug(f'out file name:{out_file_name}')
    record_time_free(station, out_file_name, start, end, timeout)
