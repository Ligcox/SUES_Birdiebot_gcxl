#include "User_TJ.h"

 void UserTask_TJ(void)
 {
	
			if (rc_in.rc_ch.st_data.ch_[ch_10_aux6] > 1700 && rc_in.rc_ch.st_data.ch_[ch_10_aux6] < 2100)
        {
					TIM_SetCompare4(TIM5,800);
				}
			else 
        {
					 TIM_SetCompare4(TIM5,1350);
				}
		
 }
 
// void UserTask_TJ(void)
// {
//	 TIM_SetCompare4(TIM5,800);
//	 MyDelayMs(3000);
//	 TIM_SetCompare4(TIM5,1350);
//	 MyDelayMs(3000);
// }
// 