class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        end=0
        counter=0
        j=0
        while end<time:
            max_end=end
            while j<len(clips) and clips[j][0]<=end:
                max_end=max(max_end, clips[j][1])
                j+=1
            if max_end==end:
                return -1
            counter+=1
            end=max_end
        return counter
        