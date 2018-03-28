while true; do 
    python3 start_tracker.py --mock --measurement humidity | hackathon_client humidity
    python3 start_tracker.py --mock --measurement acceleration | hackathon_client acceleration
    python3 start_tracker.py --mock --measurement pressure | hackathon_client pressure
    python3 start_tracker.py --mock --measurement temperature | hackathon_client temperature
    sleep 1
done

