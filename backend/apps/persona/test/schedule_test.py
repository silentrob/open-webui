import sys
import os
import random
import pandas as pd
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src_py.schedule import create_time_blocks, assign_sleep_blocks, define_activities, assign_state_probs


class TestCreateTimeBlocks(unittest.TestCase):

    def test_create_time_blocks_total_hours(self):
        activity = 'Test'
        total_hours = 10
        min_block = 1
        max_block = 3
        blocks = create_time_blocks(activity, total_hours, min_block, max_block)
        self.assertEqual(sum(blocks), total_hours)

    def test_create_time_blocks_min_max_blocks(self):
        activity = 'Test'
        total_hours = 10
        min_block = 1
        max_block = 3
        blocks = create_time_blocks(activity, total_hours, min_block, max_block)
        self.assertTrue(all(min_block <= block <= max_block for block in blocks))

    def test_create_time_blocks_remaining_hours(self):
        activity = 'Test'
        total_hours = 10
        min_block = 1
        max_block = 3
        blocks = create_time_blocks(activity, total_hours, min_block, max_block)
        self.assertEqual(sum(blocks), total_hours)

class TestAssignSleepBlocks(unittest.TestCase):

    def test_assign_sleep_blocks_first_day(self):
        schedule = pd.DataFrame(index=pd.date_range(start='2024-06-01', periods=24*7*4, freq='15min'), columns=['Activity', 'State'])
        min_block = 7
        max_block = 10
        assign_sleep_blocks(schedule, min_block, max_block)
        self.assertTrue('Sleep' in schedule['Activity'].values)
    
    def test_assign_sleep_blocks_multiple_days(self):
        schedule = pd.DataFrame(index=pd.date_range(start='2024-06-01', periods=24*7*4, freq='15min'), columns=['Activity', 'State'])
        min_block = 7
        max_block = 10
        assign_sleep_blocks(schedule, min_block, max_block)
        self.assertTrue(all(schedule['Activity'].value_counts()['Sleep'] >= 2 for _ in range(7)))

    def test_no_sleep_blocks(self):
        schedule = pd.DataFrame(index=pd.date_range(start='2024-06-01', periods=24*7*4, freq='15min'), columns=['Activity', 'State'])
        min_block = 0
        max_block = 0
        schedule = assign_sleep_blocks(schedule, min_block, max_block)
        self.assertFalse('Sleep' in schedule['Activity'].values)

    def test_minimum_block_size(self):
        schedule = pd.DataFrame(index=pd.date_range(start='2024-06-01', periods=24*7*4, freq='15min'), columns=['Activity', 'State'])
        min_block = 7
        max_block = 7
        schedule = assign_sleep_blocks(schedule, min_block, max_block)
        self.assertTrue(all(block == 'Sleep' for block in schedule['Activity'].values if block == 'Sleep'))

    def test_maximum_block_size(self):
        schedule = pd.DataFrame(index=pd.date_range(start='2024-06-01', periods=24*7*4, freq='15min'), columns=['Activity', 'State'])
        min_block = 7
        max_block = 10
        schedule = assign_sleep_blocks(schedule, min_block, max_block)
        sleep_blocks = schedule[schedule['Activity'] == 'Sleep']
        for i in range(0, len(sleep_blocks), max_block):
            self.assertTrue(len(sleep_blocks[i:i+max_block]) <= max_block)

    def test_no_overlapping_sleep_blocks(self):
        schedule = pd.DataFrame(index=pd.date_range(start='2024-06-01', periods=24*7*4, freq='15min'), columns=['Activity', 'State'])
        min_block = 7
        max_block = 10
        schedule = assign_sleep_blocks(schedule, min_block, max_block)
        sleep_blocks = schedule[schedule['Activity'] == 'Sleep']
        self.assertTrue(sleep_blocks.index.is_unique)

if __name__ == '__main__':
    unittest.main()