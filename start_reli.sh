while true; do 
    python3 start_tracker.py --mock --measurement humidity | hackathon_client humidity
    sleep 1
    python3 start_tracker.py --mock --measurement acceleration | hackathon_client acceleration
    sleep 1
    python3 start_tracker.py --mock --measurement pressure | hackathon_client pressure
    sleep 1
    python3 start_tracker.py --mock --measurement temperature | hackathon_client temperature
    sleep 5
done

