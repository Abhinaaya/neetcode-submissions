class Solution {
public:
    bool caneat(vector<int>&piles,int speed,int h)
    {
        long long hours=0;
        for(int pile:piles)
        {
            hours+=(pile+speed-1)/speed;
        }
        return hours<=h;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        
        int n=piles.size();
        int l=1;
        int r = *max_element(piles.begin(), piles.end());
        int ans=r;
        while(l<=r)
        {
            int mid=l+(r-l)/2;
            if(caneat(piles,mid,h))
            {
                ans=mid;
                r=mid-1;
            }
            else
            {
                l=mid+1;
            }
        }
        return ans;
        
    }
};
