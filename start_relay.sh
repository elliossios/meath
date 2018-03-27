while true; do 
    python start_tracker.py --mock --measurement humidity| ./wclient humidity
    python start_tracker.py --mock --measurement acceleration| ./wclient acceleration
    python start_tracker.py --mock --measurement pressure| ./wclient pressure
    python start_tracker.py --mock --measurement temperature| ./wclient temperature
    sleep 1
done

