import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--root',
            type=str,
            default='dataset/gtzan/images_original',
            required=False,
            help='Database directory')
    parser.add_argument(
            '--seed',
            type=int,
            default=0,
            required=False,
            help='set random seed')
    parser.add_argument(
            '--epochs',
            type=int,
            default=10,
            required=False,
            help='number of epochs')
    parser.add_argument(
            '--batch_size',
            type=int,
            default=16,
            required=False,
            help='Batch size')
    parser.add_argument(
            '--num_workers',
            type=int,
            default=4,
            required=False,
            help='number of workser')
    return parser.parse_args()

