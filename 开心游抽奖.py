import requests
import json
import time
import datetime

# 目标URL
url = "https://xddq.xdmanager.cn/api/lottery/draw"

# 请求头
headers = {
    "Host": "xddq.xdmanager.cn",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541739) XWEB/18955",
    "xweb_xhr": "1",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx094652b828053785/4/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

# 请求体数据
data = {
    "accountName": "luyizhi11",
    "playerId": "3119742660636",
    "gameName": "筱-橘子"
}

# 执行次数和间隔配置
total_executions = 6
interval_seconds = 120  # 2分钟 = 120秒

def send_request(request_number):
    """发送单个请求并处理响应"""
    print(f"\n{'='*60}")
    print(f"第 {request_number}/{total_executions} 次请求")
    print(f"时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"请求参数: {data}")
    
    try:
        # 发送POST请求
        response = requests.post(url, headers=headers, data=data, timeout=30)
        
        # 打印响应信息
        print(f"状态码: {response.status_code}")
        print("响应内容:")
        try:
            # 尝试解析JSON响应
            json_response = response.json()
            print(json.dumps(json_response, indent=2, ensure_ascii=False))
        except:
            # 如果不是JSON，打印原始文本
            print(response.text[:500])  # 限制输出长度
        
    except requests.exceptions.Timeout:
        print("请求超时（30秒）")
    except requests.exceptions.ConnectionError:
        print("连接错误")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")

def main():
    """主循环函数"""
    print(f"开始执行定时请求任务")
    print(f"总执行次数: {total_executions}")
    print(f"执行间隔: {interval_seconds} 秒 ({interval_seconds/60} 分钟)")
    print(f"开始时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"预计结束时间: {(datetime.datetime.now() + datetime.timedelta(seconds=interval_seconds*(total_executions-1))).strftime('%Y-%m-%d %H:%M:%S')}")
    
    for i in range(1, total_executions + 1):
        # 发送请求
        send_request(i)
        
        # 如果不是最后一次请求，等待间隔时间
        if i < total_executions:
            print(f"\n等待 {interval_seconds} 秒后执行下一次请求...")
            print(f"下次执行时间: {(datetime.datetime.now() + datetime.timedelta(seconds=interval_seconds)).strftime('%Y-%m-%d %H:%M:%S')}")
            
            # 显示倒计时
            for remaining in range(interval_seconds, 0, -1):
                if remaining % 30 == 0 or remaining <= 10:  # 每30秒或最后10秒显示一次
                    print(f"倒计时: {remaining} 秒", end='\r')
                time.sleep(1)
            print(f"{' '*20}")  # 清空倒计时行
    
    print(f"\n{'='*60}")
    print(f"任务完成！")
    print(f"完成时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"总执行次数: {total_executions}")

if __name__ == "__main__":
    main()
