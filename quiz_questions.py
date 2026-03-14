# =============================================================================
# EV ECOSYSTEM – SKILL ASSESSMENT QUIZ BANK
# =============================================================================
# 5 MCQ questions per role × 100 roles = 500 questions total
#
# Each question dict:
#   q        – question text
#   options  – dict with keys A, B, C, D
#   answer   – correct key ("A" / "B" / "C" / "D")
#   skill    – the skill being tested
#   level    – "Beginner" / "Intermediate" / "Advanced"
#
# USAGE:
#   from quiz_questions import quiz_bank, get_quiz, evaluate_quiz
#
#   questions = get_quiz("EV Battery Design Engineer")       # 5 questions
#   score, results = evaluate_quiz(user_answers, questions)
# =============================================================================

quiz_bank = {

    # =========================================================================
    # BATTERY TECHNOLOGY
    # =========================================================================

    "EV Battery Design Engineer": [
        {
            "q": "Which lithium-ion cathode chemistry offers the highest energy density but lower thermal stability?",
            "options": {"A": "LFP (LiFePO4)", "B": "NMC 811", "C": "LTO (Li4Ti5O12)", "D": "LMO (LiMn2O4)"},
            "answer": "B", "skill": "Li-ion chemistry", "level": "Intermediate"
        },
        {
            "q": "What is the primary purpose of a thermal management system in an EV battery pack?",
            "options": {"A": "Increase cell voltage", "B": "Maintain cells within safe operating temperature range", "C": "Boost state of charge", "D": "Reduce internal resistance permanently"},
            "answer": "B", "skill": "Thermal management", "level": "Beginner"
        },
        {
            "q": "Which testing standard governs the transport safety of lithium-ion batteries?",
            "options": {"A": "ISO 26262", "B": "IEC 61851", "C": "UN 38.3", "D": "SAE J2954"},
            "answer": "C", "skill": "Battery standards", "level": "Intermediate"
        },
        {
            "q": "In an equivalent circuit model (ECM) of a battery, what does the RC branch represent?",
            "options": {"A": "Open-circuit voltage", "B": "Self-discharge current", "C": "Diffusion and polarisation transient behaviour", "D": "Internal series resistance only"},
            "answer": "C", "skill": "Cell modeling", "level": "Advanced"
        },
        {
            "q": "What phenomenon causes lithium plating on the anode, leading to capacity loss and safety risks?",
            "options": {"A": "High temperature charging", "B": "Charging at very low temperatures or high C-rates", "C": "Deep discharging below 2V", "D": "Electrolyte decomposition at cathode"},
            "answer": "B", "skill": "Electrochemistry", "level": "Advanced"
        },
    ],

    "Battery Management System (BMS) Engineer": [
        {
            "q": "Which algorithm is most commonly used for real-time State of Charge (SOC) estimation in EV BMS?",
            "options": {"A": "PID controller", "B": "Extended Kalman Filter", "C": "Fourier Transform", "D": "Monte Carlo simulation"},
            "answer": "B", "skill": "SOC estimation", "level": "Advanced"
        },
        {
            "q": "What is the purpose of passive balancing in a BMS?",
            "options": {"A": "Transfer excess charge from higher cells to lower cells", "B": "Dissipate excess energy from higher-charge cells as heat", "C": "Increase overall pack capacity", "D": "Prevent thermal runaway"},
            "answer": "B", "skill": "Cell balancing", "level": "Intermediate"
        },
        {
            "q": "In AUTOSAR BMS software, which layer is responsible for hardware abstraction?",
            "options": {"A": "Application layer", "B": "RTE (Runtime Environment)", "C": "MCAL (Microcontroller Abstraction Layer)", "D": "COM stack"},
            "answer": "C", "skill": "AUTOSAR", "level": "Advanced"
        },
        {
            "q": "What does ASIL-D represent in the ISO 26262 functional safety standard?",
            "options": {"A": "Lowest risk level", "B": "No safety requirement", "C": "Highest automotive safety integrity level", "D": "Component-level testing only"},
            "answer": "C", "skill": "ISO 26262", "level": "Intermediate"
        },
        {
            "q": "What is the typical CAN bus data rate used in automotive BMS communication?",
            "options": {"A": "10 kbps", "B": "500 kbps", "C": "10 Mbps", "D": "1 Gbps"},
            "answer": "B", "skill": "CAN protocol", "level": "Beginner"
        },
    ],

    "Battery Test Technician": [
        {
            "q": "What does a HPPC (Hybrid Pulse Power Characterization) test measure?",
            "options": {"A": "Battery temperature profile", "B": "Internal resistance and power capability at various SOC levels", "C": "Electrolyte decomposition rate", "D": "Cell manufacturing defects"},
            "answer": "B", "skill": "Battery testing", "level": "Intermediate"
        },
        {
            "q": "What is a C-rate in battery testing?",
            "options": {"A": "Temperature coefficient of resistance", "B": "Charge/discharge current relative to battery capacity", "C": "Cell voltage at full charge", "D": "Coulombic efficiency percentage"},
            "answer": "B", "skill": "Battery testing", "level": "Beginner"
        },
        {
            "q": "Which standard specifically covers secondary lithium cells for portable applications safety?",
            "options": {"A": "UN 38.3", "B": "IEC 62133", "C": "ISO 26262", "D": "IEC 61851"},
            "answer": "B", "skill": "IEC 62133", "level": "Intermediate"
        },
        {
            "q": "In electrochemical impedance spectroscopy (EIS), what does the semicircle in the Nyquist plot represent?",
            "options": {"A": "Electrolyte resistance", "B": "Warburg diffusion element", "C": "Charge transfer resistance and double-layer capacitance", "D": "Open-circuit voltage"},
            "answer": "C", "skill": "EIS", "level": "Advanced"
        },
        {
            "q": "A nail penetration test is classified as which type of battery safety test?",
            "options": {"A": "Electrical abuse", "B": "Mechanical abuse", "C": "Thermal abuse", "D": "Environmental test"},
            "answer": "B", "skill": "Abuse testing", "level": "Beginner"
        },
    ],

    "Battery Cell Manufacturing Engineer": [
        {
            "q": "What is the role of the calendering process in electrode manufacturing?",
            "options": {"A": "Coat active material onto current collector", "B": "Compress electrode to improve energy density and conductivity", "C": "Fill electrolyte into the cell", "D": "Form the SEI layer"},
            "answer": "B", "skill": "Electrode manufacturing", "level": "Intermediate"
        },
        {
            "q": "What is formation cycling in cell manufacturing?",
            "options": {"A": "First charge/discharge cycles that form the SEI layer and activate the cell", "B": "Final quality check using X-ray", "C": "Electrolyte injection process", "D": "Welding of cell tabs"},
            "answer": "A", "skill": "Formation cycling", "level": "Intermediate"
        },
        {
            "q": "Which Six Sigma tool is used to identify and prioritise root causes of manufacturing defects?",
            "options": {"A": "Control chart", "B": "Fishbone (Ishikawa) diagram", "C": "Gantt chart", "D": "Pareto chart only"},
            "answer": "B", "skill": "Six Sigma", "level": "Beginner"
        },
        {
            "q": "Why is a dry-room environment (low dew point) critical in battery cell manufacturing?",
            "options": {"A": "To prevent static electricity", "B": "To keep operators comfortable", "C": "To prevent moisture contamination of electrodes and electrolyte", "D": "To improve electrode coating speed"},
            "answer": "C", "skill": "Cleanroom protocols", "level": "Intermediate"
        },
        {
            "q": "What does a process Cpk value greater than 1.33 indicate?",
            "options": {"A": "Process is out of control", "B": "Process is capable and centred within specification limits", "C": "Too many defects are being produced", "D": "Sample size is insufficient"},
            "answer": "B", "skill": "Process control", "level": "Advanced"
        },
    ],

    "EV Battery Recycling Specialist": [
        {
            "q": "What is 'Black Mass' in battery recycling?",
            "options": {"A": "Carbon black used in electrodes", "B": "Shredded mixture of cathode and anode active materials", "C": "Residual electrolyte after draining", "D": "Slag from smelting process"},
            "answer": "B", "skill": "Battery recycling", "level": "Intermediate"
        },
        {
            "q": "Which recycling method recovers lithium at highest purity by dissolving materials in acid solutions?",
            "options": {"A": "Pyrometallurgy", "B": "Direct recycling", "C": "Hydrometallurgy", "D": "Mechanical shredding only"},
            "answer": "C", "skill": "Hydrometallurgy", "level": "Advanced"
        },
        {
            "q": "Before dismantling an EV battery pack for recycling, what is the mandatory first step?",
            "options": {"A": "Remove the BMS", "B": "Fully discharge the pack to safe voltage levels", "C": "Weigh the pack", "D": "Remove coolant pipes"},
            "answer": "B", "skill": "Safety protocols", "level": "Beginner"
        },
        {
            "q": "What does 'direct recycling' aim to preserve in spent battery materials?",
            "options": {"A": "Only the copper current collector", "B": "The crystalline structure of cathode material for re-use", "C": "Electrolyte solvents", "D": "Battery pack casing"},
            "answer": "B", "skill": "Direct recycling", "level": "Advanced"
        },
        {
            "q": "Which regulation requires battery manufacturers to track battery composition and recyclability?",
            "options": {"A": "ISO 26262", "B": "EU Battery Passport Regulation", "C": "IEC 61851", "D": "UNECE WP.29"},
            "answer": "B", "skill": "Battery passport", "level": "Intermediate"
        },
    ],

    "EV Battery Safety Tester": [
        {
            "q": "An overcharge test is performed to simulate which real-world failure scenario?",
            "options": {"A": "Cell short circuit", "B": "BMS failure allowing voltage to exceed maximum limits", "C": "Coolant leak", "D": "Connector corrosion"},
            "answer": "B", "skill": "Abuse testing", "level": "Intermediate"
        },
        {
            "q": "What temperature range typically triggers thermal runaway in NMC lithium-ion cells?",
            "options": {"A": "20–40°C", "B": "60–80°C", "C": "130–180°C", "D": "Over 300°C only"},
            "answer": "C", "skill": "Thermal analysis", "level": "Advanced"
        },
        {
            "q": "What does AIS-048 govern in the Indian EV context?",
            "options": {"A": "Charging connector standards", "B": "Battery safety requirements for electric vehicles", "C": "Motor efficiency ratings", "D": "EV registration process"},
            "answer": "B", "skill": "Safety standards", "level": "Intermediate"
        },
        {
            "q": "What instrument is used to measure internal resistance of a battery cell?",
            "options": {"A": "Oscilloscope", "B": "Milliohm meter / LCR meter", "C": "Multimeter set to DC voltage", "D": "Torque wrench"},
            "answer": "B", "skill": "Battery testing", "level": "Beginner"
        },
        {
            "q": "During a thermal propagation test, what is being validated?",
            "options": {"A": "Charge acceptance rate", "B": "That thermal runaway in one cell does not spread to adjacent cells causing pack-level failure", "C": "Coolant flow rate", "D": "BMS communication latency"},
            "answer": "B", "skill": "Thermal runaway", "level": "Advanced"
        },
    ],

    "EV Battery Algorithm Developer": [
        {
            "q": "What is the main advantage of the Extended Kalman Filter (EKF) over the standard Kalman Filter for SOC estimation?",
            "options": {"A": "Simpler to implement", "B": "Handles non-linear battery dynamics through linearisation", "C": "Requires no initial SOC estimate", "D": "Works without a battery model"},
            "answer": "B", "skill": "Kalman filter", "level": "Advanced"
        },
        {
            "q": "Which model parameter represents the rate of self-discharge in an equivalent circuit battery model?",
            "options": {"A": "Series resistance R0", "B": "Parallel RC branch", "C": "Leakage resistance (Rp) in parallel with OCV", "D": "Warburg element"},
            "answer": "C", "skill": "Cell modeling", "level": "Advanced"
        },
        {
            "q": "What does RUL stand for in battery prognostics?",
            "options": {"A": "Rated Usable Limit", "B": "Remaining Useful Life", "C": "Relative Utilisation Level", "D": "Resistance Under Load"},
            "answer": "B", "skill": "RUL estimation", "level": "Beginner"
        },
        {
            "q": "In MATLAB/Simulink, which toolbox is specifically designed for battery modelling and SOC estimation?",
            "options": {"A": "Signal Processing Toolbox", "B": "Powertrain Blockset", "C": "Control System Toolbox", "D": "Curve Fitting Toolbox"},
            "answer": "B", "skill": "MATLAB/Simulink", "level": "Intermediate"
        },
        {
            "q": "What metric is used to quantify battery degradation as a fraction of original capacity?",
            "options": {"A": "SOC (State of Charge)", "B": "SOP (State of Power)", "C": "SOH (State of Health)", "D": "DOD (Depth of Discharge)"},
            "answer": "C", "skill": "SOH estimation", "level": "Beginner"
        },
    ],

    "EV Battery Thermal Analyst": [
        {
            "q": "In CFD simulation of a battery pack, what boundary condition is applied at the cell surface for heat generation?",
            "options": {"A": "Constant pressure outlet", "B": "Volumetric heat source based on Joule heating and entropy change", "C": "Zero-flux Neumann condition", "D": "Ambient temperature Dirichlet condition"},
            "answer": "B", "skill": "CFD", "level": "Advanced"
        },
        {
            "q": "What is the purpose of phase change material (PCM) in battery thermal management?",
            "options": {"A": "Improve electrical conductivity", "B": "Absorb and release latent heat to buffer temperature spikes", "C": "Replace liquid coolant entirely", "D": "Insulate cells from vibration"},
            "answer": "B", "skill": "Thermal management", "level": "Intermediate"
        },
        {
            "q": "Which COMSOL module is used for electrochemical-thermal coupled battery simulation?",
            "options": {"A": "CFD Module", "B": "Battery Design Module", "C": "Structural Mechanics Module", "D": "RF Module"},
            "answer": "B", "skill": "COMSOL", "level": "Intermediate"
        },
        {
            "q": "What is the Biot number (Bi) used to determine in thermal analysis?",
            "options": {"A": "Whether convection or conduction dominates heat transfer within a solid", "B": "Fluid flow regime (laminar vs turbulent)", "C": "Heat generation rate in electrodes", "D": "Coolant pressure drop"},
            "answer": "A", "skill": "Thermal simulations", "level": "Advanced"
        },
        {
            "q": "In liquid-cooled EV battery packs, what fluid is most commonly used as coolant?",
            "options": {"A": "Pure water", "B": "Engine oil", "C": "Glycol-water mixture (50:50)", "D": "Liquid nitrogen"},
            "answer": "C", "skill": "Thermal management", "level": "Beginner"
        },
    ],

    "EV Battery Economic Analyst": [
        {
            "q": "What does TCO (Total Cost of Ownership) analysis include for EV batteries?",
            "options": {"A": "Only purchase price", "B": "Purchase price, maintenance, energy costs, and end-of-life disposal", "C": "Battery weight only", "D": "Manufacturing yield rates"},
            "answer": "B", "skill": "TCO modeling", "level": "Beginner"
        },
        {
            "q": "The current benchmark cost target for EV battery packs is approximately:",
            "options": {"A": "Over $500/kWh", "B": "Around $100/kWh at pack level", "C": "$10/kWh", "D": "$1000/kWh"},
            "answer": "B", "skill": "Battery economics", "level": "Intermediate"
        },
        {
            "q": "In a DCF (Discounted Cash Flow) model, a higher discount rate results in:",
            "options": {"A": "Higher NPV", "B": "Lower NPV, making future cash flows worth less today", "C": "No change in NPV", "D": "Increased IRR"},
            "answer": "B", "skill": "DCF analysis", "level": "Intermediate"
        },
        {
            "q": "Which raw material represents the highest cost component in an NMC battery cathode?",
            "options": {"A": "Lithium", "B": "Manganese", "C": "Cobalt", "D": "Nickel (in NMC 811)"},
            "answer": "D", "skill": "Battery economics", "level": "Advanced"
        },
        {
            "q": "What does a sensitivity analysis in financial modelling test?",
            "options": {"A": "Physical durability of components", "B": "How changes in key assumptions impact the final financial output", "C": "Statistical significance of data", "D": "Employee performance"},
            "answer": "B", "skill": "Scenario analysis", "level": "Intermediate"
        },
    ],

    "EV Cell Characterization Scientist": [
        {
            "q": "What does the low-frequency tail in an EIS Nyquist plot represent?",
            "options": {"A": "Electrolyte bulk resistance", "B": "Charge transfer at electrode surface", "C": "Solid-state diffusion (Warburg impedance)", "D": "SEI layer resistance"},
            "answer": "C", "skill": "EIS", "level": "Advanced"
        },
        {
            "q": "GITT (Galvanostatic Intermittent Titration Technique) is used to determine:",
            "options": {"A": "Battery capacity fade rate", "B": "Solid-state lithium diffusion coefficient in electrode", "C": "Thermal runaway onset temperature", "D": "CAN bus latency"},
            "answer": "B", "skill": "Cell characterization", "level": "Advanced"
        },
        {
            "q": "What is Coulombic Efficiency (CE) and what does near-100% CE indicate?",
            "options": {"A": "Voltage efficiency; ideal charging", "B": "Ratio of discharge to charge capacity; minimal side reactions", "C": "Temperature coefficient; stable operation", "D": "Power factor; minimal reactive power"},
            "answer": "B", "skill": "Battery characterization", "level": "Intermediate"
        },
        {
            "q": "Differential Voltage Analysis (dV/dQ) is used to:",
            "options": {"A": "Measure thermal conductivity", "B": "Identify phase transitions and capacity loss mechanisms in aged cells", "C": "Calculate power output", "D": "Test mechanical strength"},
            "answer": "B", "skill": "Degradation analysis", "level": "Advanced"
        },
        {
            "q": "What is the significance of the SEI (Solid Electrolyte Interphase) layer?",
            "options": {"A": "It increases electrode conductivity", "B": "It forms on the anode, consuming lithium but enabling stable long-term cycling", "C": "It prevents temperature rise", "D": "It replaces the separator"},
            "answer": "B", "skill": "Electrochemistry", "level": "Intermediate"
        },
    ],

    "EV Battery Pack Assembly Lead": [
        {
            "q": "What joining method is most commonly used to weld nickel tabs to cylindrical Li-ion cells in a module?",
            "options": {"A": "Arc welding", "B": "Laser welding or ultrasonic welding", "C": "Soldering", "D": "Mechanical crimping only"},
            "answer": "B", "skill": "Cell joining", "level": "Intermediate"
        },
        {
            "q": "What does an EOL (End of Line) test verify on an assembled battery pack?",
            "options": {"A": "Cell chemistry", "B": "Complete electrical, communication, and leak checks before shipment", "C": "Module weight", "D": "Cathode material purity"},
            "answer": "B", "skill": "EOL testing", "level": "Beginner"
        },
        {
            "q": "What IP rating is typically required for an EV battery pack enclosure?",
            "options": {"A": "IP20", "B": "IP44", "C": "IP67", "D": "IP10"},
            "answer": "C", "skill": "Pack design", "level": "Intermediate"
        },
        {
            "q": "In a PFMEA for battery pack assembly, what does the RPN (Risk Priority Number) help determine?",
            "options": {"A": "Production throughput", "B": "Severity × Occurrence × Detection to prioritise failure modes", "C": "Material cost per unit", "D": "Operator training hours"},
            "answer": "B", "skill": "FMEA", "level": "Intermediate"
        },
        {
            "q": "During HV (High Voltage) battery handling in assembly, which PPE is mandatory?",
            "options": {"A": "Standard safety glasses only", "B": "Insulated gloves rated for the system voltage, face shield, and arc flash suit", "C": "Hard hat only", "D": "Steel-toed boots only"},
            "answer": "B", "skill": "HV safety", "level": "Beginner"
        },
    ],

    # =========================================================================
    # POWER ELECTRONICS & MOTOR SYSTEMS
    # =========================================================================

    "Power Electronics Engineer": [
        {
            "q": "What is the main advantage of SiC MOSFETs over silicon IGBTs in EV traction inverters?",
            "options": {"A": "Lower cost", "B": "Higher switching frequency with lower switching losses enabling higher efficiency", "C": "Better short circuit withstand time", "D": "Lower gate drive voltage"},
            "answer": "B", "skill": "SiC MOSFETs", "level": "Advanced"
        },
        {
            "q": "What is the purpose of a dead-time in a half-bridge inverter switch pattern?",
            "options": {"A": "Increase switching frequency", "B": "Prevent shoot-through by ensuring both switches are never ON simultaneously", "C": "Reduce gate drive power", "D": "Filter output harmonics"},
            "answer": "B", "skill": "Inverter design", "level": "Intermediate"
        },
        {
            "q": "In a buck converter, when the duty cycle D = 0.6 and input voltage Vin = 400V, what is the output voltage?",
            "options": {"A": "400V", "B": "666V", "C": "240V", "D": "160V"},
            "answer": "C", "skill": "DC-DC converters", "level": "Intermediate"
        },
        {
            "q": "What does CISPR 25 Class 5 limit specify?",
            "options": {"A": "Battery cycle life", "B": "Strictest electromagnetic interference limits for automotive receivers", "C": "Motor efficiency classification", "D": "PCB copper weight"},
            "answer": "B", "skill": "EMI/EMC", "level": "Advanced"
        },
        {
            "q": "What is the function of a bootstrap circuit in a high-side gate driver?",
            "options": {"A": "Provide overcurrent protection", "B": "Supply a floating gate drive voltage above the high-side switch source", "C": "Filter PWM noise", "D": "Measure IGBT temperature"},
            "answer": "B", "skill": "Gate driver design", "level": "Advanced"
        },
    ],

    "EV Motor Control Engineer": [
        {
            "q": "In Field-Oriented Control (FOC), why are stator currents transformed to a rotating d-q reference frame?",
            "options": {"A": "To simplify wiring", "B": "To decouple torque (q-axis) and flux (d-axis) control like a DC machine", "C": "To reduce motor speed", "D": "To measure back-EMF directly"},
            "answer": "B", "skill": "FOC", "level": "Advanced"
        },
        {
            "q": "What is the purpose of field weakening in an EV traction motor?",
            "options": {"A": "Increase motor torque at low speeds", "B": "Extend operating speed beyond base speed by reducing d-axis flux", "C": "Improve power factor", "D": "Reduce winding temperature"},
            "answer": "B", "skill": "Motor control", "level": "Advanced"
        },
        {
            "q": "Which modulation technique reduces harmonic content in a 3-phase inverter output compared to basic sinusoidal PWM?",
            "options": {"A": "Hysteresis control", "B": "Space Vector PWM (SVPWM)", "C": "Square wave switching", "D": "Delta modulation"},
            "answer": "B", "skill": "SVPWM", "level": "Intermediate"
        },
        {
            "q": "What sensor is eliminated in sensorless motor control, and what replaces it?",
            "options": {"A": "Current sensor; replaced by voltage estimation", "B": "Position/speed encoder; replaced by back-EMF or observer-based estimation", "C": "Temperature sensor; replaced by thermal model", "D": "Torque sensor; replaced by power measurement"},
            "answer": "B", "skill": "Sensorless control", "level": "Advanced"
        },
        {
            "q": "In a PI current controller for FOC, what does increasing the integral gain (Ki) do?",
            "options": {"A": "Increases rise time", "B": "Eliminates steady-state error faster but risks overshoot/instability", "C": "Reduces bandwidth", "D": "Has no effect on steady state"},
            "answer": "B", "skill": "Control systems", "level": "Intermediate"
        },
    ],

    "EV Powertrain Engineer": [
        {
            "q": "What is the primary purpose of a single-speed gearbox (reducer) in an EV powertrain?",
            "options": {"A": "Provide multiple gear ratios", "B": "Step down motor speed and multiply torque for wheel delivery", "C": "Disconnect motor during regeneration", "D": "Absorb NVH from the road"},
            "answer": "B", "skill": "Powertrain design", "level": "Beginner"
        },
        {
            "q": "Torque vectoring in an EV with dual motors improves:",
            "options": {"A": "Battery life only", "B": "Lateral vehicle dynamics and cornering by independently controlling wheel torques", "C": "Charging speed", "D": "Cabin heating efficiency"},
            "answer": "B", "skill": "Torque vectoring", "level": "Intermediate"
        },
        {
            "q": "What phenomenon does NVH analysis in EV drivetrains specifically address that is different from ICE vehicles?",
            "options": {"A": "Combustion noise masking", "B": "High-frequency whine from gear mesh and motor harmonics that are no longer masked by engine noise", "C": "Exhaust gas resonance", "D": "Fuel injector click"},
            "answer": "B", "skill": "NVH analysis", "level": "Advanced"
        },
        {
            "q": "In GT-Suite simulation, what type of analysis is used to optimise EV powertrain efficiency over a drive cycle?",
            "options": {"A": "FEA structural analysis", "B": "Forward-looking or backward-looking quasi-static simulation over WLTP/UDDS cycle", "C": "CFD fluid analysis", "D": "Monte Carlo reliability analysis"},
            "answer": "B", "skill": "Powertrain simulation", "level": "Advanced"
        },
        {
            "q": "An e-axle integrates which three main components?",
            "options": {"A": "Battery, BMS, charger", "B": "Electric motor, gearbox/reducer, and inverter", "C": "Motor, brake caliper, and wheel hub", "D": "Inverter, DC-DC converter, OBC"},
            "answer": "B", "skill": "E-axle design", "level": "Intermediate"
        },
    ],

    "EV Calibration Engineer": [
        {
            "q": "What is the XCP (Universal Measurement and Calibration Protocol) used for?",
            "options": {"A": "Charging communication", "B": "Real-time ECU measurement and calibration via CAN/Ethernet", "C": "Motor control communication", "D": "Battery cell balancing"},
            "answer": "B", "skill": "ECU calibration", "level": "Advanced"
        },
        {
            "q": "What file format (A2L) is used in AUTOSAR calibration workflows?",
            "options": {"A": "Describes physical layout of PCB", "B": "ASAP2 format describing ECU memory layout for calibration parameters", "C": "Video format for test recordings", "D": "Binary flash image"},
            "answer": "B", "skill": "Calibration tools", "level": "Intermediate"
        },
        {
            "q": "During dyno testing of an EV powertrain, what parameter is the calibration engineer primarily optimising?",
            "options": {"A": "Cabin temperature", "B": "Motor torque maps, efficiency maps, and control strategy parameters", "C": "Tyre pressure", "D": "Suspension stiffness"},
            "answer": "B", "skill": "Dyno testing", "level": "Intermediate"
        },
        {
            "q": "Model-Based Calibration (MBC) in MATLAB uses what mathematical approach?",
            "options": {"A": "Finite element method", "B": "Design of Experiments (DoE) and statistical response surface models", "C": "Monte Carlo simulation", "D": "Genetic algorithms exclusively"},
            "answer": "B", "skill": "MATLAB/Simulink", "level": "Advanced"
        },
        {
            "q": "What is flash programming / ECU flashing used for during vehicle calibration?",
            "options": {"A": "Taking photographs of vehicle", "B": "Writing updated software and calibration data into ECU memory", "C": "Testing battery voltage", "D": "Checking brake pad wear"},
            "answer": "B", "skill": "ECU calibration", "level": "Beginner"
        },
    ],

    "EV Wireless Charging Engineer": [
        {
            "q": "What does SAE J2954 define for EV wireless charging?",
            "options": {"A": "Wired connector standards", "B": "Interoperability requirements for wireless power transfer including power levels, frequency, and FOD", "C": "Battery chemistry requirements", "D": "Motor efficiency classes"},
            "answer": "B", "skill": "SAE J2954", "level": "Intermediate"
        },
        {
            "q": "In resonant inductive charging, why are coils operated at their resonant frequency?",
            "options": {"A": "To generate heat", "B": "To maximise power transfer efficiency by minimising reactive power", "C": "To reduce coil size", "D": "To comply with FCC regulations"},
            "answer": "B", "skill": "Inductive charging", "level": "Advanced"
        },
        {
            "q": "What does FOD (Foreign Object Detection) prevent in wireless EV charging?",
            "options": {"A": "Software bugs", "B": "Metallic objects near the charging pad from heating up due to induced eddy currents", "C": "Unauthorised vehicle charging", "D": "Battery overcharge"},
            "answer": "B", "skill": "FOD", "level": "Intermediate"
        },
        {
            "q": "What is the typical operating frequency range for EV wireless power transfer per SAE J2954?",
            "options": {"A": "50–60 Hz (mains frequency)", "B": "85 kHz ± 10%", "C": "1–10 MHz", "D": "2.4 GHz (WiFi band)"},
            "answer": "B", "skill": "WPT design", "level": "Advanced"
        },
        {
            "q": "Misalignment tolerance in wireless charging refers to:",
            "options": {"A": "Voltage mismatch between charger and vehicle", "B": "Maximum lateral/longitudinal offset between transmitter and receiver coils while maintaining acceptable efficiency", "C": "Phase difference in AC supply", "D": "Temperature variance"},
            "answer": "B", "skill": "Alignment systems", "level": "Intermediate"
        },
    ],

    # =========================================================================
    # EMBEDDED SOFTWARE & FIRMWARE
    # =========================================================================

    "EV Software Developer": [
        {
            "q": "In AUTOSAR Classic, what is the role of the RTE (Runtime Environment)?",
            "options": {"A": "Manage hardware peripherals", "B": "Provide communication middleware between SWCs and BSW, abstracting hardware", "C": "Handle CAN bus arbitration", "D": "Store calibration data"},
            "answer": "B", "skill": "AUTOSAR", "level": "Advanced"
        },
        {
            "q": "What does MISRA C:2012 Rule 15.5 mandate regarding functions?",
            "options": {"A": "Functions must be inlined", "B": "A function should have a single point of exit", "C": "Recursion is allowed", "D": "All variables must be global"},
            "answer": "B", "skill": "MISRA-C", "level": "Advanced"
        },
        {
            "q": "In UDS (ISO 14229), what service ID (0x27) is used for?",
            "options": {"A": "Read Data by Identifier", "B": "Security Access – used to unlock ECU for diagnostic operations", "C": "Communication Control", "D": "ECU Reset"},
            "answer": "B", "skill": "UDS diagnostics", "level": "Intermediate"
        },
        {
            "q": "What is the CAN arbitration mechanism that ensures higher priority messages always win bus access?",
            "options": {"A": "TDMA (Time Division Multiple Access)", "B": "CSMA/CA with bitwise non-destructive arbitration (lower ID = higher priority)", "C": "Token ring protocol", "D": "Round-robin scheduling"},
            "answer": "B", "skill": "CAN protocol", "level": "Intermediate"
        },
        {
            "q": "In a CI/CD pipeline for embedded software, what does a hardware-in-the-loop (HIL) test stage validate?",
            "options": {"A": "Code formatting", "B": "Software behaviour against real or simulated hardware signals before vehicle integration", "C": "Database migrations", "D": "UI rendering"},
            "answer": "B", "skill": "CI/CD", "level": "Intermediate"
        },
    ],

    "Embedded Systems Engineer": [
        {
            "q": "What is the key difference between a hard real-time system and a soft real-time system?",
            "options": {"A": "Hard systems use C, soft systems use Python", "B": "In hard real-time, missing a deadline causes system failure; in soft real-time, occasional misses are tolerable", "C": "Hard systems have more memory", "D": "Soft systems run on microcontrollers"},
            "answer": "B", "skill": "RTOS", "level": "Intermediate"
        },
        {
            "q": "What is JTAG primarily used for in embedded systems development?",
            "options": {"A": "Power management", "B": "In-circuit debugging, boundary scan testing, and programming of microcontrollers", "C": "CAN communication", "D": "OTA updates"},
            "answer": "B", "skill": "JTAG debugging", "level": "Beginner"
        },
        {
            "q": "In FreeRTOS, what mechanism prevents two tasks from accessing a shared resource simultaneously?",
            "options": {"A": "Interrupt nesting", "B": "Mutex (mutual exclusion semaphore)", "C": "Memory protection unit", "D": "DMA transfer"},
            "answer": "B", "skill": "FreeRTOS", "level": "Intermediate"
        },
        {
            "q": "What does AUTOSAR MCAL stand for and what is its function?",
            "options": {"A": "Motor Control Abstraction Layer; controls inverter", "B": "Microcontroller Abstraction Layer; standardises access to MCU peripherals", "C": "Memory Cache Abstraction Logic; manages RAM", "D": "Module Calibration Access Layer; stores parameters"},
            "answer": "B", "skill": "AUTOSAR", "level": "Advanced"
        },
        {
            "q": "Why is DMA (Direct Memory Access) used in embedded systems?",
            "options": {"A": "To increase CPU clock speed", "B": "To transfer data between peripherals and memory without CPU intervention, freeing CPU for other tasks", "C": "To encrypt communication", "D": "To provide power management"},
            "answer": "B", "skill": "DMA", "level": "Intermediate"
        },
    ],

    "EV Firmware Developer": [
        {
            "q": "What is the role of a bootloader in an embedded microcontroller?",
            "options": {"A": "Manage battery state", "B": "Initialise hardware and allow application firmware to be loaded or updated", "C": "Handle CAN messages", "D": "Run the main application directly"},
            "answer": "B", "skill": "Bootloader", "level": "Beginner"
        },
        {
            "q": "What is the primary security concern addressed by secure boot?",
            "options": {"A": "Preventing unauthorised CAN messages", "B": "Ensuring only cryptographically verified firmware runs on the device", "C": "Protecting user passwords", "D": "Encrypting sensor data"},
            "answer": "B", "skill": "Secure boot", "level": "Intermediate"
        },
        {
            "q": "In OTA (Over-The-Air) firmware updates for EVs, what is a critical requirement to prevent bricking?",
            "options": {"A": "Fastest possible download", "B": "Atomic update with rollback capability if verification fails", "C": "Disabling BMS during update", "D": "Requiring vehicle to be in motion"},
            "answer": "B", "skill": "OTA updates", "level": "Advanced"
        },
        {
            "q": "What is the hardware abstraction layer (HAL) in firmware development?",
            "options": {"A": "A circuit board layer", "B": "Software layer that provides a standard interface to hardware, making application code hardware-independent", "C": "A type of communication protocol", "D": "Memory management unit"},
            "answer": "B", "skill": "HAL", "level": "Intermediate"
        },
        {
            "q": "FOTA (Firmware Over The Air) for EV chargers uses which protocol for campaign management in the OCPP context?",
            "options": {"A": "MQTT", "B": "OCPP UpdateFirmware message", "C": "FTP only", "D": "Bluetooth LE"},
            "answer": "B", "skill": "FOTA", "level": "Advanced"
        },
    ],

    "EV Firmware Security Engineer": [
        {
            "q": "What is side-channel analysis in the context of embedded security?",
            "options": {"A": "Analysing CAN bus traffic", "B": "Extracting secret keys by measuring physical signals like power consumption or electromagnetic emissions", "C": "Testing secondary communication channels", "D": "Reviewing unused code paths"},
            "answer": "B", "skill": "Side-channel analysis", "level": "Advanced"
        },
        {
            "q": "What does AUTOSAR SecOC provide in vehicle communication security?",
            "options": {"A": "Encrypted OTA updates", "B": "Message Authentication Code (MAC) to verify authenticity of CAN/Ethernet messages", "C": "Secure key storage", "D": "Firewall between ECUs"},
            "answer": "B", "skill": "AUTOSAR SecOC", "level": "Advanced"
        },
        {
            "q": "What is fuzzing used for in firmware security testing?",
            "options": {"A": "Making code readable", "B": "Sending malformed/random inputs to find vulnerabilities and crashes", "C": "Measuring power consumption", "D": "Compiling firmware"},
            "answer": "B", "skill": "Fuzzing", "level": "Intermediate"
        },
        {
            "q": "An HSM (Hardware Security Module) in an automotive ECU is primarily used to:",
            "options": {"A": "Add more RAM", "B": "Securely store cryptographic keys and perform crypto operations in hardware-isolated environment", "C": "Provide CAN transceiver functions", "D": "Handle OBD-II diagnostics"},
            "answer": "B", "skill": "HSM", "level": "Advanced"
        },
        {
            "q": "What does a SBOM (Software Bill of Materials) list?",
            "options": {"A": "Hardware components", "B": "All software components, libraries, and dependencies in a product for vulnerability tracking", "C": "Manufacturing costs", "D": "Test results"},
            "answer": "B", "skill": "SBOM", "level": "Intermediate"
        },
    ],

    "EV Charger Firmware Developer": [
        {
            "q": "In OCPP 1.6, which message does a charge point send to notify the backend that it has started a charging session?",
            "options": {"A": "Heartbeat", "B": "StartTransaction", "C": "Authorize", "D": "MeterValues"},
            "answer": "B", "skill": "OCPP", "level": "Intermediate"
        },
        {
            "q": "What is the purpose of a watchdog timer in charger firmware?",
            "options": {"A": "Measure charging current", "B": "Reset the MCU if the firmware hangs or enters an infinite loop", "C": "Time session duration", "D": "Monitor cable temperature"},
            "answer": "B", "skill": "Firmware", "level": "Intermediate"
        },
        {
            "q": "What does IEC 61851-1 define for EV charging?",
            "options": {"A": "Battery chemistry requirements", "B": "Conductive EV charging system requirements including control pilot (CP) signal", "C": "OCPP backend protocol", "D": "Wireless charging frequency"},
            "answer": "B", "skill": "IEC 61851", "level": "Intermediate"
        },
        {
            "q": "In the IEC 61851 control pilot state machine, what does State C indicate?",
            "options": {"A": "EV not connected", "B": "EV connected and charging with ventilation required", "C": "EV connected, ready to charge (no ventilation needed)", "D": "Fault condition"},
            "answer": "C", "skill": "Control pilot", "level": "Advanced"
        },
        {
            "q": "What version control workflow is recommended for collaborative firmware development?",
            "options": {"A": "Emailing zip files", "B": "Git with feature branching and pull request reviews", "C": "FTP server with versioned folders", "D": "Single shared master branch with no reviews"},
            "answer": "B", "skill": "Git", "level": "Beginner"
        },
    ],

    # =========================================================================
    # ADAS & AUTONOMY
    # =========================================================================

    "Autonomous Driving Software Engineer": [
        {
            "q": "What does SLAM stand for and what problem does it solve?",
            "options": {"A": "Speed Limit and Motion; cruise control", "B": "Simultaneous Localisation and Mapping; building a map while tracking the vehicle position within it", "C": "Sensor Layer and Merging; combining sensor data", "D": "Static Landmark and Matching; recognising signs"},
            "answer": "B", "skill": "SLAM", "level": "Advanced"
        },
        {
            "q": "In a ROS2 architecture, what is a 'topic'?",
            "options": {"A": "A configuration file", "B": "A named bus over which nodes publish and subscribe to messages asynchronously", "C": "A service call that expects a response", "D": "A parameter server entry"},
            "answer": "B", "skill": "ROS2", "level": "Intermediate"
        },
        {
            "q": "TensorRT optimises deep learning models for inference by:",
            "options": {"A": "Increasing model accuracy", "B": "Quantisation, layer fusion, and kernel auto-tuning for NVIDIA GPU deployment", "C": "Retraining the model with more data", "D": "Converting PyTorch to TensorFlow"},
            "answer": "B", "skill": "TensorRT", "level": "Advanced"
        },
        {
            "q": "What is the difference between a ROS2 service and a topic?",
            "options": {"A": "Services are faster", "B": "Services are synchronous request-response; topics are asynchronous publish-subscribe", "C": "Topics require authentication", "D": "Services only work with LiDAR"},
            "answer": "B", "skill": "ROS2", "level": "Intermediate"
        },
        {
            "q": "In sensor fusion for ADAS, why is LiDAR data often fused with camera data?",
            "options": {"A": "LiDAR provides colour information", "B": "LiDAR provides accurate 3D depth/geometry while camera provides rich texture and semantic information", "C": "Camera provides distance measurement", "D": "LiDAR works better in daylight"},
            "answer": "B", "skill": "Sensor fusion", "level": "Intermediate"
        },
    ],

    "EV Navigation System Developer": [
        {
            "q": "What is dead reckoning in EV navigation?",
            "options": {"A": "Using GPS exclusively", "B": "Estimating position using last known location + speed/heading from IMU when GPS signal is lost", "C": "Mapping road hazards", "D": "Range prediction algorithm"},
            "answer": "B", "skill": "Navigation", "level": "Intermediate"
        },
        {
            "q": "What makes EV navigation routing different from standard vehicle routing?",
            "options": {"A": "EVs follow different traffic rules", "B": "EV routing must factor in remaining range, charging station locations, and route energy consumption", "C": "EV maps have different road types", "D": "EVs cannot use highways"},
            "answer": "B", "skill": "EV routing", "level": "Beginner"
        },
        {
            "q": "The NMEA 0183 protocol is used for:",
            "options": {"A": "CAN bus communication", "B": "Standardised GPS/GNSS data output from receivers to navigation systems", "C": "Wireless charging control", "D": "OCPP backend communication"},
            "answer": "B", "skill": "GNSS", "level": "Intermediate"
        },
        {
            "q": "Dijkstra's algorithm is used in navigation for:",
            "options": {"A": "Image processing", "B": "Finding the shortest path between nodes in a weighted graph (road network)", "C": "Sensor calibration", "D": "Map rendering"},
            "answer": "B", "skill": "Routing algorithms", "level": "Intermediate"
        },
        {
            "q": "What is map matching in navigation?",
            "options": {"A": "Comparing two different maps", "B": "Snapping raw GPS coordinates onto the road network to determine actual road position", "C": "Matching vehicle speed to speed limits", "D": "Aligning sensor axes"},
            "answer": "B", "skill": "Map matching", "level": "Intermediate"
        },
    ],

    # =========================================================================
    # CHARGING INFRASTRUCTURE
    # =========================================================================

    "EV Charging Infrastructure Planner": [
        {
            "q": "What does OCPP 2.0.1 add over OCPP 1.6 that is significant for smart charging?",
            "options": {"A": "Faster payment processing", "B": "Device management, smart charging profiles, 15118 Plug & Charge, and improved security", "C": "More connector types", "D": "Higher voltage support"},
            "answer": "B", "skill": "OCPP", "level": "Advanced"
        },
        {
            "q": "What is V2G (Vehicle-to-Grid) technology?",
            "options": {"A": "GPS navigation for EVs", "B": "Bidirectional power flow allowing EV batteries to discharge energy back to the electricity grid", "C": "Vehicle wireless software update", "D": "Vehicle-to-garage door opener"},
            "answer": "B", "skill": "V2G", "level": "Beginner"
        },
        {
            "q": "Load forecasting for EV charging sites is important because:",
            "options": {"A": "It determines vehicle speed", "B": "It helps size grid connection, avoid peak demand charges, and plan charging schedules", "C": "It calculates driver route", "D": "It monitors battery chemistry"},
            "answer": "B", "skill": "Load forecasting", "level": "Intermediate"
        },
        {
            "q": "ISO 15118 enables 'Plug & Charge' — what does this mean?",
            "options": {"A": "The charger auto-detects AC or DC", "B": "The EV authenticates and authorises payment automatically when plugged in, without RFID or app", "C": "The plug self-locks", "D": "The charger adjusts voltage automatically"},
            "answer": "B", "skill": "ISO 15118", "level": "Advanced"
        },
        {
            "q": "What is the maximum power level for AC charging in a typical 3-phase 32A installation?",
            "options": {"A": "3.3 kW", "B": "7.4 kW", "C": "22 kW", "D": "50 kW"},
            "answer": "C", "skill": "Charging standards", "level": "Intermediate"
        },
    ],

    "Fast Charger Field Technician": [
        {
            "q": "Before working on a DC fast charger, which lockout/tagout (LOTO) step is first?",
            "options": {"A": "Remove the charger cover", "B": "Isolate the power supply and verify zero energy state with a meter", "C": "Reboot the charger software", "D": "Call the customer"},
            "answer": "B", "skill": "HV safety", "level": "Beginner"
        },
        {
            "q": "CCS (Combined Charging System) uses which standard for DC fast charging communication?",
            "options": {"A": "CHAdeMO", "B": "ISO 15118 / DIN 70121 over PLC on the CP line", "C": "OCPP over cellular", "D": "Bluetooth LE"},
            "answer": "B", "skill": "CCS standard", "level": "Intermediate"
        },
        {
            "q": "What does an insulation resistance test (Megger test) verify in a charging installation?",
            "options": {"A": "Charging speed", "B": "That insulation between conductors and earth is adequate (typically >1MΩ)", "C": "OCPP connectivity", "D": "Touch screen functionality"},
            "answer": "B", "skill": "Insulation testing", "level": "Intermediate"
        },
        {
            "q": "What is the control pilot (CP) signal in IEC 61851, and what does a 1 kHz PWM duty cycle indicate?",
            "options": {"A": "Battery temperature signal; cell SOC", "B": "Pilot signal between EVSE and EV; duty cycle encodes maximum available charging current", "C": "Grounding continuity; cable integrity", "D": "OCPP heartbeat; connection status"},
            "answer": "B", "skill": "IEC 61851", "level": "Advanced"
        },
        {
            "q": "An OCPP StatusNotification message with status 'Faulted' means:",
            "options": {"A": "Charger is idle", "B": "Charger has detected an error and is unable to charge", "C": "Session is complete", "D": "Charger is reserved"},
            "answer": "B", "skill": "OCPP diagnostics", "level": "Intermediate"
        },
    ],

    "EV Charging Network Analyst": [
        {
            "q": "What KPI is most important for measuring EV charging network reliability?",
            "options": {"A": "Number of connectors", "B": "Uptime percentage (availability of chargers to dispense energy when requested)", "C": "Network revenue", "D": "Number of registered users"},
            "answer": "B", "skill": "Uptime KPIs", "level": "Beginner"
        },
        {
            "q": "In GIS analysis for charging network planning, which spatial analysis helps identify underserved areas?",
            "options": {"A": "Choropleth mapping", "B": "Service area analysis / isochrone mapping around existing chargers", "C": "DEM (Digital Elevation Model) analysis", "D": "Satellite image classification"},
            "answer": "B", "skill": "GIS", "level": "Intermediate"
        },
        {
            "q": "A charging session with high utilisation but low revenue per session most likely indicates:",
            "options": {"A": "Charger hardware fault", "B": "Pricing is too low or sessions are too short (dwell time issue)", "C": "OCPP firmware bug", "D": "Grid outage"},
            "answer": "B", "skill": "Network analytics", "level": "Intermediate"
        },
        {
            "q": "What does the OCPP MeterValues message report?",
            "options": {"A": "Charger location coordinates", "B": "Real-time energy delivered, power, current, voltage during an active session", "C": "User authentication result", "D": "Firmware version"},
            "answer": "B", "skill": "OCPP analytics", "level": "Advanced"
        },
        {
            "q": "To predict charging demand at a new site, which data source is most relevant?",
            "options": {"A": "Vehicle paint colour data", "B": "EV registration density, traffic patterns, and nearby POI (points of interest)", "C": "Social media sentiment", "D": "Weather data only"},
            "answer": "B", "skill": "Load forecasting", "level": "Intermediate"
        },
    ],

    "EV Charging Site Planner": [
        {
            "q": "What is a key output document from a charging site survey before installation?",
            "options": {"A": "Vehicle service history", "B": "Single Line Diagram (SLD) showing grid connection, transformer, and EVSE layout", "C": "Battery chemistry report", "D": "OCPP backend configuration"},
            "answer": "B", "skill": "Site planning", "level": "Beginner"
        },
        {
            "q": "Why is grid capacity assessment critical before deploying a fleet of DC fast chargers?",
            "options": {"A": "To choose cable colours", "B": "To ensure the local grid connection can supply sufficient peak power without overload or costly upgrades", "C": "To determine charger colour scheme", "D": "To calculate driver routes"},
            "answer": "B", "skill": "Grid integration", "level": "Intermediate"
        },
        {
            "q": "What is demand charge management in the context of charging site economics?",
            "options": {"A": "Charging customers more at peak hours", "B": "Strategies to reduce peak power draw (load management, scheduling) to minimise utility demand charges", "C": "Managing customer complaints", "D": "Forecasting EV sales"},
            "answer": "B", "skill": "Load forecasting", "level": "Advanced"
        },
        {
            "q": "In AutoCAD, what standard drawing is produced to show cable routing and conduit paths for a charging site?",
            "options": {"A": "Floor plan for aesthetics", "B": "Electrical installation drawing / cable schedule", "C": "Structural beam layout", "D": "Plumbing diagram"},
            "answer": "B", "skill": "AutoCAD", "level": "Beginner"
        },
        {
            "q": "What does a net metering agreement with a distribution company allow at a charging site with solar PV?",
            "options": {"A": "Free electricity", "B": "Excess solar generation to be exported to the grid and credited against consumption", "C": "Bypass safety inspections", "D": "Install unlimited chargers"},
            "answer": "B", "skill": "Grid integration", "level": "Intermediate"
        },
    ],

    "EV Charging Hardware Designer": [
        {
            "q": "What IP rating is required for outdoor DC fast charger enclosures exposed to rain?",
            "options": {"A": "IP20", "B": "IP54 minimum (dust protected, splash proof)", "C": "IP10", "D": "IP00"},
            "answer": "B", "skill": "Enclosure design", "level": "Beginner"
        },
        {
            "q": "IEC 62196 specifies standards for:",
            "options": {"A": "Battery cell chemistry", "B": "EV charging connectors and inlets including Type 1, Type 2, CCS", "C": "OCPP protocol messages", "D": "Grid connection voltage levels"},
            "answer": "B", "skill": "IEC 62196", "level": "Intermediate"
        },
        {
            "q": "During PCB layout of a high-current EV charger power stage, why are wide copper pours and short traces critical?",
            "options": {"A": "Aesthetic reasons", "B": "To minimise parasitic inductance, resistance, and temperature rise in high-current paths", "C": "To meet IEC 61851 protocol", "D": "To reduce component count"},
            "answer": "B", "skill": "PCB design", "level": "Advanced"
        },
        {
            "q": "What is the function of an RCCB (Residual Current Circuit Breaker) in an EVSE installation?",
            "options": {"A": "Limit charging power", "B": "Detect earth leakage/fault current and disconnect supply to prevent electric shock", "C": "Measure energy delivered", "D": "Provide overcurrent protection"},
            "answer": "B", "skill": "Safety standards", "level": "Intermediate"
        },
        {
            "q": "Pre-compliance EMC testing on a charger prototype is performed to:",
            "options": {"A": "Measure charging efficiency", "B": "Identify EMI issues early before costly formal certification testing", "C": "Validate OCPP messages", "D": "Test user interface"},
            "answer": "B", "skill": "EMI/EMC", "level": "Intermediate"
        },
    ],

    "EV Charging Site Electrician": [
        {
            "q": "What tool is used to verify earth continuity in an EV charging installation?",
            "options": {"A": "Clamp ammeter", "B": "Low-resistance ohmmeter / continuity tester", "C": "Oscilloscope", "D": "Lux meter"},
            "answer": "B", "skill": "Testing", "level": "Beginner"
        },
        {
            "q": "When installing cable for a 150 kW DC fast charger, the cable sizing must account for:",
            "options": {"A": "Only the charger brand", "B": "Current carrying capacity, voltage drop, fault level, and ambient temperature derating", "C": "Colour coding preferences", "D": "OCPP version"},
            "answer": "B", "skill": "Electrical installation", "level": "Intermediate"
        },
        {
            "q": "What does a Type B RCCB detect that a Type A does not?",
            "options": {"A": "Overloads", "B": "Smooth DC fault currents in addition to AC and pulsating DC fault currents", "C": "Short circuits", "D": "Voltage surges"},
            "answer": "B", "skill": "Safety standards", "level": "Advanced"
        },
        {
            "q": "Before energising a new EVSE installation, which test must confirm correct phase rotation?",
            "options": {"A": "Insulation resistance test", "B": "Phase sequence test using a phase rotation meter", "C": "OCPP ping test", "D": "Earth electrode resistance test"},
            "answer": "B", "skill": "Commissioning", "level": "Intermediate"
        },
        {
            "q": "What PPE must always be worn when working on live LV panels during a permitted task?",
            "options": {"A": "Standard work boots only", "B": "Insulated gloves rated to system voltage, face shield, and arc flash-rated clothing", "C": "Hi-vis vest only", "D": "Safety glasses only"},
            "answer": "B", "skill": "HV safety", "level": "Beginner"
        },
    ],

    "EV Charging Site Electrician II": [
        {
            "q": "What does power quality analysis measure at a charging site?",
            "options": {"A": "Charging session count", "B": "Voltage harmonics, THD, power factor, flicker, and sags/swells on the supply", "C": "Battery temperature", "D": "OCPP message frequency"},
            "answer": "B", "skill": "Power quality", "level": "Advanced"
        },
        {
            "q": "Why is earthing design critical for a charging hub?",
            "options": {"A": "For aesthetic grounding", "B": "To provide fault current return path, limit touch voltages, and protect personnel during faults", "C": "To meet colour code requirements", "D": "To enable WiFi connectivity"},
            "answer": "B", "skill": "Earthing", "level": "Intermediate"
        },
        {
            "q": "A thermal imaging camera during EVSE inspection reveals a hotspot on a cable termination. This indicates:",
            "options": {"A": "Normal operation", "B": "Loose connection causing increased resistance and heat — requires immediate retorquing", "C": "High ambient temperature", "D": "Charger is at full power"},
            "answer": "B", "skill": "Thermal imaging", "level": "Intermediate"
        },
        {
            "q": "What is the purpose of an RCD (Residual Current Device) Type EV specifically for EV chargers?",
            "options": {"A": "Faster charging", "B": "Detects all fault current types (AC, pulsating DC, smooth DC) specific to EV charger leakage profiles", "C": "Measures energy delivered", "D": "Provides overload protection only"},
            "answer": "B", "skill": "Safety standards", "level": "Advanced"
        },
        {
            "q": "What regulation governs electrical installation inspection and testing requirements in India?",
            "options": {"A": "IEC 61851", "B": "IS 732 (Indian Standard for Electrical Wiring) and CEA Regulations", "C": "OCPP 2.0.1", "D": "ISO 26262"},
            "answer": "B", "skill": "Electrical standards", "level": "Intermediate"
        },
    ],

    "EV Charging Operations Supervisor": [
        {
            "q": "An SLA typically guarantees charging network uptime of at least:",
            "options": {"A": "50%", "B": "95–99% depending on contract tier", "C": "100%", "D": "75%"},
            "answer": "B", "skill": "SLA management", "level": "Beginner"
        },
        {
            "q": "When a charger goes offline remotely, what OCPP message does the backend use to attempt a restart?",
            "options": {"A": "StartTransaction", "B": "Reset (soft or hard) request to the charge point", "C": "Heartbeat", "D": "DataTransfer"},
            "answer": "B", "skill": "OCPP", "level": "Intermediate"
        },
        {
            "q": "What is a key metric in a NOC (Network Operations Centre) dashboard for charger fleet management?",
            "options": {"A": "Vehicle colour", "B": "Charger availability rate, active faults, sessions per day, and energy dispensed", "C": "Driver name", "D": "Battery chemistry"},
            "answer": "B", "skill": "Network operations", "level": "Intermediate"
        },
        {
            "q": "Preventive maintenance scheduling for DC fast chargers typically includes:",
            "options": {"A": "Painting the charger", "B": "Filter cleaning, connector inspection, cable check, firmware update, and insulation test", "C": "Replacing the entire unit annually", "D": "Repainting markings only"},
            "answer": "B", "skill": "Maintenance", "level": "Intermediate"
        },
        {
            "q": "A MTTR (Mean Time To Repair) of 4 hours vs 12 hours indicates:",
            "options": {"A": "Higher failure rate", "B": "Faster incident resolution, higher service quality", "C": "More failures", "D": "Lower uptime"},
            "answer": "B", "skill": "KPIs", "level": "Beginner"
        },
    ],

    "EV Charging Reliability Engineer": [
        {
            "q": "In Weibull analysis, a shape parameter β < 1 indicates:",
            "options": {"A": "Wear-out failures", "B": "Decreasing failure rate (infant mortality / early life failures)", "C": "Constant failure rate", "D": "Random failures only"},
            "answer": "B", "skill": "Weibull analysis", "level": "Advanced"
        },
        {
            "q": "MTBF (Mean Time Between Failures) is calculated as:",
            "options": {"A": "Total failures / operating hours", "B": "Total operating hours / number of failures", "C": "Total repair time / failures", "D": "Failure rate × time"},
            "answer": "B", "skill": "MTBF", "level": "Intermediate"
        },
        {
            "q": "What is the purpose of HALT (Highly Accelerated Life Testing)?",
            "options": {"A": "Test software bugs", "B": "Expose design weaknesses by applying extreme stress (temperature, vibration) beyond operating limits", "C": "Certify the product for sale", "D": "Measure energy efficiency"},
            "answer": "B", "skill": "HALT", "level": "Intermediate"
        },
        {
            "q": "In a fault tree analysis (FTA) for a charging station, an AND gate means:",
            "options": {"A": "Any one input causes the top event", "B": "All input events must occur simultaneously for the output event to occur", "C": "The top event is impossible", "D": "Only one input is considered"},
            "answer": "B", "skill": "Fault tree analysis", "level": "Advanced"
        },
        {
            "q": "FMEA RPN (Risk Priority Number) = Severity × Occurrence × Detection. A high Detection score means:",
            "options": {"A": "The failure is easily detected", "B": "The failure is very difficult to detect before it reaches the customer", "C": "The failure occurs rarely", "D": "The failure has low impact"},
            "answer": "B", "skill": "FMEA", "level": "Intermediate"
        },
    ],

    "EV Charging API Developer": [
        {
            "q": "In REST API design for an EV charging backend, which HTTP method is used to update a charging session resource?",
            "options": {"A": "GET", "B": "PUT or PATCH", "C": "DELETE", "D": "OPTIONS"},
            "answer": "B", "skill": "REST APIs", "level": "Beginner"
        },
        {
            "q": "What does OCPI (Open Charge Point Interface) enable?",
            "options": {"A": "Charger to vehicle communication", "B": "Roaming between different CPO and eMSP networks for EV drivers", "C": "Battery management", "D": "Wireless charging"},
            "answer": "B", "skill": "OCPI protocol", "level": "Intermediate"
        },
        {
            "q": "OAuth 2.0 in a charging API is used for:",
            "options": {"A": "Database encryption", "B": "Secure delegated authorisation — allowing third-party apps to access APIs on behalf of users", "C": "WebSocket handshake", "D": "Hardware authentication"},
            "answer": "B", "skill": "OAuth", "level": "Intermediate"
        },
        {
            "q": "What does an OpenAPI (Swagger) specification provide?",
            "options": {"A": "Database schema", "B": "Machine-readable description of REST API endpoints, request/response formats for documentation and code generation", "C": "Firmware binary", "D": "Network topology"},
            "answer": "B", "skill": "API documentation", "level": "Intermediate"
        },
        {
            "q": "OCPP uses WebSocket as transport. What advantage does WebSocket provide over HTTP polling for charger communication?",
            "options": {"A": "Better security", "B": "Persistent bidirectional connection enabling real-time server-to-charger push messages", "C": "Simpler implementation", "D": "Lower bandwidth always"},
            "answer": "B", "skill": "OCPP", "level": "Advanced"
        },
    ],

    "EV Charging Payment Systems Developer": [
        {
            "q": "What does PCI-DSS compliance require for storing cardholder data?",
            "options": {"A": "Store everything in plain text for auditability", "B": "Protect cardholder data with encryption, restrict access, and avoid storing CVV after authorisation", "C": "Use only local databases", "D": "Allow all employees access"},
            "answer": "B", "skill": "PCI-DSS", "level": "Intermediate"
        },
        {
            "q": "Tokenisation in payment systems replaces sensitive card data with:",
            "options": {"A": "Encrypted card number stored locally", "B": "A unique non-sensitive token that references the actual data stored securely by the payment processor", "C": "A QR code", "D": "User's email address"},
            "answer": "B", "skill": "Tokenisation", "level": "Intermediate"
        },
        {
            "q": "What does OCPI CDR (Charge Detail Record) contain that is relevant to payment?",
            "options": {"A": "User's driving history", "B": "Session duration, energy delivered, tariff applied, and total cost for billing reconciliation", "C": "Charger hardware version", "D": "OCPP firmware version"},
            "answer": "B", "skill": "OCPI protocol", "level": "Advanced"
        },
        {
            "q": "In a microservices architecture for a charging platform, what does an API gateway provide?",
            "options": {"A": "Database storage", "B": "Single entry point for clients with routing, authentication, rate limiting, and load balancing", "C": "OCPP server", "D": "Payment terminal hardware"},
            "answer": "B", "skill": "Microservices", "level": "Advanced"
        },
        {
            "q": "Dynamic pricing in EV charging means:",
            "options": {"A": "Price is always fixed", "B": "Tariff varies based on time-of-use, grid demand, or user type to optimise load and revenue", "C": "Free charging during peak hours", "D": "Price per connector type"},
            "answer": "B", "skill": "Charging economics", "level": "Intermediate"
        },
    ],

    "EV Charging Network Security Lead": [
        {
            "q": "What is OT (Operational Technology) security in the context of EV charging infrastructure?",
            "options": {"A": "Office IT security", "B": "Securing industrial control systems and physical devices like chargers, PLCs, and SCADA from cyber threats", "C": "Securing customer mobile apps", "D": "Encrypting billing data only"},
            "answer": "B", "skill": "OT security", "level": "Advanced"
        },
        {
            "q": "Network segmentation in a charging hub separates the charger OCPP network from corporate IT to:",
            "options": {"A": "Reduce cable costs", "B": "Limit the blast radius of a breach — preventing attackers from moving laterally between networks", "C": "Improve charging speed", "D": "Comply with OCPP 1.6"},
            "answer": "B", "skill": "Network security", "level": "Advanced"
        },
        {
            "q": "A vulnerability assessment differs from a penetration test in that:",
            "options": {"A": "Vulnerability assessment is illegal", "B": "VA identifies and categorises vulnerabilities without exploiting them; pentest actively exploits to demonstrate impact", "C": "Pentest only scans for open ports", "D": "VA requires physical access"},
            "answer": "B", "skill": "Vulnerability assessment", "level": "Intermediate"
        },
        {
            "q": "What is SIEM (Security Information and Event Management) used for in network security?",
            "options": {"A": "Managing charger firmware", "B": "Collecting, correlating, and analysing security logs from across the network to detect threats in real time", "C": "Processing payments", "D": "Managing WiFi access"},
            "answer": "B", "skill": "SIEM", "level": "Intermediate"
        },
        {
            "q": "OCPP 2.0.1 introduced security profiles to address which gap in OCPP 1.6?",
            "options": {"A": "Faster message delivery", "B": "Lack of TLS encryption and message authentication in charger-backend communication", "C": "Support for more connector types", "D": "Mobile app integration"},
            "answer": "B", "skill": "OCPP security", "level": "Advanced"
        },
    ],

    "EV Charge Point Operator (CPO)": [
        {
            "q": "What is the primary role of a Charge Point Operator (CPO)?",
            "options": {"A": "Manufacture EV batteries", "B": "Own, operate, and maintain EV charging infrastructure and ensure availability for end users", "C": "Design motor control algorithms", "D": "Regulate EV policy"},
            "answer": "B", "skill": "CPO operations", "level": "Beginner"
        },
        {
            "q": "What does eMSP stand for in EV charging ecosystem?",
            "options": {"A": "Electric Motor Speed Protocol", "B": "Electric Mobility Service Provider — offers charging access and billing services to EV drivers across networks", "C": "Energy Management System Protocol", "D": "EV Motor Safety Protocol"},
            "answer": "B", "skill": "EV ecosystem", "level": "Intermediate"
        },
        {
            "q": "Energy billing for EV charging can be structured as kWh-based or time-based. Why is kWh-based preferred?",
            "options": {"A": "It is simpler to measure", "B": "It is fairer as drivers pay for actual energy received regardless of charging speed", "C": "It requires no metering", "D": "It is mandated by OCPP"},
            "answer": "B", "skill": "Energy billing", "skill": "Billing", "level": "Intermediate"
        },
        {
            "q": "In an OCPP network, Heartbeat messages serve to:",
            "options": {"A": "Send energy readings", "B": "Confirm the charge point is still online and synchronise its clock with the backend", "C": "Start a charging session", "D": "Update firmware"},
            "answer": "B", "skill": "OCPP", "level": "Beginner"
        },
        {
            "q": "What is the key revenue model for a CPO operating public charging stations?",
            "options": {"A": "Selling EV batteries", "B": "Charging fees (per kWh or time), network membership fees, and grid services revenue", "C": "Manufacturing chargers", "D": "Selling EV insurance"},
            "answer": "B", "skill": "Business model", "level": "Beginner"
        },
    ],

    "EV Charger UX Designer": [
        {
            "q": "In HMI design for EV chargers, what principle ensures users always know the system state?",
            "options": {"A": "Minimalism", "B": "Nielsen's 'Visibility of System Status' — always keeping users informed through clear feedback", "C": "Skeuomorphism", "D": "Dark mode"},
            "answer": "B", "skill": "HMI design", "level": "Intermediate"
        },
        {
            "q": "WCAG 2.1 Level AA contrast ratio requirement for normal text is:",
            "options": {"A": "2:1", "B": "4.5:1", "C": "7:1", "D": "1:1"},
            "answer": "B", "skill": "Accessibility", "level": "Intermediate"
        },
        {
            "q": "When designing a multilingual charging kiosk UI, what technical consideration is critical?",
            "options": {"A": "Font size only", "B": "Text expansion (some languages need 30–40% more space) and RTL (right-to-left) support", "C": "Colour scheme", "D": "Animation speed"},
            "answer": "B", "skill": "UI design", "level": "Advanced"
        },
        {
            "q": "What is a Figma component library used for in design teams?",
            "options": {"A": "Version control for code", "B": "Reusable UI elements that maintain consistency and allow global style updates across all designs", "C": "Backend API documentation", "D": "User interview recordings"},
            "answer": "B", "skill": "Design systems", "level": "Intermediate"
        },
        {
            "q": "A heuristic evaluation of a charging app identifies 'Error Prevention' issues. This means:",
            "options": {"A": "Users are making too many purchases", "B": "The design does not prevent users from making mistakes before they occur", "C": "Error messages are missing", "D": "The app crashes frequently"},
            "answer": "B", "skill": "Usability", "level": "Intermediate"
        },
    ],

    "EV Charging UX Researcher": [
        {
            "q": "What research method provides the richest insight into how real users interact with a charging kiosk?",
            "options": {"A": "Online survey alone", "B": "Contextual inquiry — observing users in their natural context at a real charging station", "C": "Focus group in office", "D": "A/B email campaign"},
            "answer": "B", "skill": "User research", "level": "Intermediate"
        },
        {
            "q": "What is affinity mapping used for in UX research?",
            "options": {"A": "Creating wireframes", "B": "Organising qualitative research data into clusters of related insights and themes", "C": "Writing user stories", "D": "Building prototypes"},
            "answer": "B", "skill": "Research methods", "level": "Intermediate"
        },
        {
            "q": "Net Promoter Score (NPS) in a charging network context measures:",
            "options": {"A": "Network uptime", "B": "Likelihood of users recommending the charging service to others (customer loyalty proxy)", "C": "Energy dispensed", "D": "Technical reliability"},
            "answer": "B", "skill": "CX metrics", "level": "Beginner"
        },
        {
            "q": "Think-aloud protocol in usability testing asks participants to:",
            "options": {"A": "Read a script", "B": "Verbalise their thoughts, actions, and reactions while using the product", "C": "Answer a questionnaire after use", "D": "Complete tasks silently and be timed"},
            "answer": "B", "skill": "Usability testing", "level": "Intermediate"
        },
        {
            "q": "What is a Jobs To Be Done (JTBD) framework used for in UX?",
            "options": {"A": "HR recruitment", "B": "Understanding the underlying goal or 'job' a user is trying to accomplish, beyond surface-level features", "C": "Sprint planning", "D": "A/B testing"},
            "answer": "B", "skill": "UX frameworks", "level": "Intermediate"
        },
    ],

    "EV Infrastructure Commissioning Lead": [
        {
            "q": "What is a FAT (Factory Acceptance Test) in EV charging infrastructure?",
            "options": {"A": "Financial Audit Test", "B": "Testing of equipment at the manufacturer's facility before shipment to verify it meets specifications", "C": "Site soil analysis", "D": "Environmental impact assessment"},
            "answer": "B", "skill": "Commissioning", "level": "Intermediate"
        },
        {
            "q": "A SAT (Site Acceptance Test) differs from FAT in that:",
            "options": {"A": "SAT is done in a lab", "B": "SAT is conducted on-site after installation to verify complete system integration in final environment", "C": "SAT tests software only", "D": "SAT is done before manufacturing"},
            "answer": "B", "skill": "Commissioning", "level": "Intermediate"
        },
        {
            "q": "What does a snag list document during commissioning?",
            "options": {"A": "Team lunch orders", "B": "Outstanding defects, incomplete works, and issues to be rectified before project handover", "C": "Energy meter readings", "D": "Cable colour codes"},
            "answer": "B", "skill": "Project management", "level": "Beginner"
        },
        {
            "q": "During HV cable jointing on a commissioning project, which document must be signed before work starts?",
            "options": {"A": "Weather report", "B": "Permit to Work (PTW) with isolation certificate and risk assessment", "C": "OCPP configuration sheet", "D": "User manual"},
            "answer": "B", "skill": "HV safety", "level": "Intermediate"
        },
        {
            "q": "Protection relay testing during commissioning verifies:",
            "options": {"A": "UI colour scheme", "B": "That the relay trips the breaker correctly within specified time when fault current thresholds are reached", "C": "OCPP connectivity", "D": "Battery pack temperature"},
            "answer": "B", "skill": "Protection testing", "level": "Advanced"
        },
    ],

    # =========================================================================
    # DATA, AI & CLOUD
    # =========================================================================

    "EV Data Analyst": [
        {
            "q": "What is the purpose of a window function in SQL for EV telemetry analysis?",
            "options": {"A": "Filtering rows", "B": "Performing calculations across a set of rows related to the current row (e.g., running total, lag/lead)", "C": "Joining two tables", "D": "Creating indexes"},
            "answer": "B", "skill": "SQL", "level": "Advanced"
        },
        {
            "q": "In Tableau, what is a calculated field used for?",
            "options": {"A": "Connecting to new data sources", "B": "Creating new data fields from existing fields using formulas for custom metrics and dimensions", "C": "Publishing to Tableau Server", "D": "Formatting axis labels"},
            "answer": "B", "skill": "Tableau", "level": "Intermediate"
        },
        {
            "q": "What does the pandas `.groupby()` function do in Python data analysis?",
            "options": {"A": "Sorts data alphabetically", "B": "Splits data into groups based on criteria, applies a function, and combines results", "C": "Removes duplicate rows", "D": "Transposes the DataFrame"},
            "answer": "B", "skill": "Python", "level": "Intermediate"
        },
        {
            "q": "Why is time-series data from EV telematics often resampled before analysis?",
            "options": {"A": "To increase data volume", "B": "To align data from sensors with different sampling rates and fill gaps for consistent analysis", "C": "To remove all outliers", "D": "To add more variables"},
            "answer": "B", "skill": "Telemetry analysis", "level": "Intermediate"
        },
        {
            "q": "What is the difference between correlation and causation in data analysis?",
            "options": {"A": "They mean the same thing", "B": "Correlation shows variables move together; causation proves one variable directly causes change in another", "C": "Causation is always easier to prove", "D": "Correlation requires experiments"},
            "answer": "B", "skill": "Statistical analysis", "level": "Beginner"
        },
    ],

    "EV Machine Learning Engineer": [
        {
            "q": "What is the key advantage of LSTM networks over standard RNNs for battery state prediction?",
            "options": {"A": "Simpler architecture", "B": "LSTM gates prevent vanishing gradient, enabling learning of long-term temporal dependencies", "C": "LSTMs require less data", "D": "LSTMs are fully explainable"},
            "answer": "B", "skill": "LSTM", "level": "Advanced"
        },
        {
            "q": "In MLOps, what does model drift refer to?",
            "options": {"A": "Model accidentally deleted", "B": "Degradation of model performance over time as input data distribution changes from training data", "C": "Model moving to different cloud region", "D": "Increasing inference speed"},
            "answer": "B", "skill": "MLOps", "level": "Intermediate"
        },
        {
            "q": "What is quantisation in the context of edge AI model deployment?",
            "options": {"A": "Adding more parameters", "B": "Reducing model precision (e.g., FP32 to INT8) to decrease model size and inference latency on edge hardware", "C": "Training with more epochs", "D": "Increasing batch size"},
            "answer": "B", "skill": "Edge AI deployment", "level": "Advanced"
        },
        {
            "q": "What is federated learning and why is it useful for EV fleet ML?",
            "options": {"A": "Training a central model with all data in one place", "B": "Training models locally on each vehicle and sharing only model updates (not raw data) to protect privacy", "C": "Using government-funded datasets", "D": "Training on simulated data only"},
            "answer": "B", "skill": "Federated learning", "level": "Advanced"
        },
        {
            "q": "MLflow is used to track which of the following in ML experiments?",
            "options": {"A": "User authentication", "B": "Model parameters, metrics, artefacts, and dataset versions for reproducibility", "C": "Database queries", "D": "Network bandwidth"},
            "answer": "B", "skill": "MLflow", "level": "Intermediate"
        },
    ],

    "EV Warranty Data Scientist": [
        {
            "q": "Survival analysis in warranty analytics is used to model:",
            "options": {"A": "Product sales trends", "B": "Time-to-failure distribution and probability of a component surviving beyond a given time", "C": "Customer satisfaction scores", "D": "Supply chain delays"},
            "answer": "B", "skill": "Survival analysis", "level": "Advanced"
        },
        {
            "q": "A Kaplan-Meier curve in reliability analysis shows:",
            "options": {"A": "Revenue over time", "B": "Estimated survival probability of components over time, accounting for censored observations", "C": "Cumulative warranty claims cost", "D": "Component weight distribution"},
            "answer": "B", "skill": "Survival analysis", "level": "Advanced"
        },
        {
            "q": "What is a warranty accrual rate used for in finance?",
            "options": {"A": "Measuring customer satisfaction", "B": "Estimating the percentage of revenue set aside as a reserve to cover expected future warranty costs", "C": "Tracking parts inventory", "D": "Calculating sales commission"},
            "answer": "B", "skill": "Warranty economics", "level": "Intermediate"
        },
        {
            "q": "Which Python library is best suited for time-series warranty failure rate analysis?",
            "options": {"A": "Flask", "B": "lifelines (survival analysis) or statsmodels (statistical time-series)", "C": "Django", "D": "Pygame"},
            "answer": "B", "skill": "Python", "level": "Intermediate"
        },
        {
            "q": "Early warning detection in warranty analytics uses which technique to find components failing faster than expected?",
            "options": {"A": "Linear regression", "B": "Statistical process control (control charts) or anomaly detection on failure rate trends", "C": "Neural image classification", "D": "A/B testing"},
            "answer": "B", "skill": "Predictive analytics", "level": "Intermediate"
        },
    ],

    "EV Digital Twin Engineer": [
        {
            "q": "What is a digital twin in the EV context?",
            "options": {"A": "A backup copy of software", "B": "A real-time virtual replica of a physical EV component or system that mirrors its behaviour using live sensor data", "C": "A duplicate vehicle for testing", "D": "A twin-motor powertrain"},
            "answer": "B", "skill": "Digital twin", "level": "Beginner"
        },
        {
            "q": "What does the FMI (Functional Mock-up Interface) standard enable?",
            "options": {"A": "CAN bus communication", "B": "Co-simulation between different modelling tools by defining a standard model exchange format (FMU)", "C": "Battery cell testing", "D": "OCPP charging communication"},
            "answer": "B", "skill": "FMI/FMU", "level": "Advanced"
        },
        {
            "q": "Modelica is used in digital twin development because:",
            "options": {"A": "It is a web programming language", "B": "It is an equation-based, object-oriented modelling language ideal for multi-physics system simulation", "C": "It runs only on supercomputers", "D": "It is proprietary to MATLAB"},
            "answer": "B", "skill": "Modelica", "level": "Intermediate"
        },
        {
            "q": "Azure Digital Twins service enables:",
            "options": {"A": "Local embedded development", "B": "Building knowledge graphs of physical environments and assets with live IoT data integration", "C": "GPU training of ML models", "D": "On-premise database hosting"},
            "answer": "B", "skill": "Azure Digital Twins", "level": "Intermediate"
        },
        {
            "q": "Why is real-time simulation (e.g., dSPACE) preferred over offline simulation for digital twin validation?",
            "options": {"A": "It is cheaper", "B": "It allows hardware-in-the-loop testing where the digital model interacts with real ECUs in real time", "C": "It requires no model", "D": "It only works for battery simulation"},
            "answer": "B", "skill": "Real-time simulation", "level": "Advanced"
        },
    ],

    "EV Cloud Integration Engineer": [
        {
            "q": "What is the MQTT QoS level 2 guarantee?",
            "options": {"A": "At most once delivery (fire and forget)", "B": "Exactly once delivery — the most reliable but highest overhead QoS level", "C": "At least once delivery", "D": "No delivery guarantee"},
            "answer": "B", "skill": "MQTT", "level": "Advanced"
        },
        {
            "q": "In Kubernetes, what is the function of a ConfigMap?",
            "options": {"A": "Store container images", "B": "Store non-sensitive configuration data as key-value pairs, decoupled from container images", "C": "Manage network policies", "D": "Define resource limits"},
            "answer": "B", "skill": "Kubernetes", "level": "Intermediate"
        },
        {
            "q": "AWS IoT Core is used in EV telematics to:",
            "options": {"A": "Train ML models", "B": "Connect, authenticate, and route MQTT messages from millions of EV devices to cloud services", "C": "Store vehicle images", "D": "Process payments"},
            "answer": "B", "skill": "AWS", "level": "Intermediate"
        },
        {
            "q": "Terraform is classified as Infrastructure as Code (IaC). Its main benefit is:",
            "options": {"A": "Writing application code", "B": "Declaratively provisioning and managing cloud infrastructure reproducibly through version-controlled code", "C": "Monitoring application performance", "D": "Containerising applications"},
            "answer": "B", "skill": "Terraform", "level": "Intermediate"
        },
        {
            "q": "InfluxDB is chosen for EV telemetry storage because it is optimised for:",
            "options": {"A": "Relational transactional data", "B": "Time-series data with high write throughput and fast time-range queries", "C": "Document storage like MongoDB", "D": "Graph relationships"},
            "answer": "B", "skill": "InfluxDB", "level": "Intermediate"
        },
    ],

    "EV Infrastructure Data Engineer": [
        {
            "q": "What is the purpose of the dbt (data build tool) in a data pipeline?",
            "options": {"A": "Real-time data streaming", "B": "Transform raw data in the warehouse using SQL, with version control and testing", "C": "Ingest raw data from APIs", "D": "Visualise dashboards"},
            "answer": "B", "skill": "dbt", "level": "Intermediate"
        },
        {
            "q": "In Apache Airflow, a DAG (Directed Acyclic Graph) defines:",
            "options": {"A": "Database schema", "B": "Workflow of tasks with dependencies, scheduled and executed in order", "C": "ML model architecture", "D": "API endpoints"},
            "answer": "B", "skill": "Apache Airflow", "level": "Intermediate"
        },
        {
            "q": "What is data lineage in data engineering?",
            "options": {"A": "Data sorted by age", "B": "Tracking the origin, transformation, and movement of data across systems for auditability", "C": "Archiving old records", "D": "Compressing data files"},
            "answer": "B", "skill": "Data quality", "level": "Intermediate"
        },
        {
            "q": "Why is a star schema preferred over normalised tables in a data warehouse for dashboard queries?",
            "options": {"A": "It uses less storage", "B": "It enables faster analytical queries with fewer joins by denormalising into fact and dimension tables", "C": "It is easier to update", "D": "It supports ACID transactions better"},
            "answer": "B", "skill": "Data modeling", "level": "Advanced"
        },
        {
            "q": "ETL stands for Extract, Transform, Load. In modern EV data platforms, ELT (Load first) is preferred because:",
            "options": {"A": "ELT is more secure", "B": "Cloud warehouses can transform data at scale after loading, enabling raw data preservation and flexible re-transformation", "C": "ELT requires no coding", "D": "ELT is faster for streaming"},
            "answer": "B", "skill": "ETL pipelines", "level": "Advanced"
        },
    ],

    "EV Fleet Telematics Manager": [
        {
            "q": "Geofencing in fleet telematics is used to:",
            "options": {"A": "Decorate the fleet tracking map", "B": "Trigger alerts or actions when a vehicle enters or exits a defined geographic boundary", "C": "Measure battery voltage", "D": "Schedule vehicle service"},
            "answer": "B", "skill": "Geofencing", "level": "Beginner"
        },
        {
            "q": "What CAN data parameter is most useful for predicting EV battery degradation in a fleet?",
            "options": {"A": "Door open/close events", "B": "State of Health (SOH) trend, temperature during charging, and fast charge frequency", "C": "Windscreen wiper usage", "D": "Seat adjustment position"},
            "answer": "B", "skill": "CAN data analysis", "level": "Intermediate"
        },
        {
            "q": "Driver behaviour scoring in fleet telematics typically analyses:",
            "options": {"A": "Music playlist", "B": "Harsh braking, rapid acceleration, speeding events, and efficient regeneration usage", "C": "Cabin temperature settings", "D": "Phone brand"},
            "answer": "B", "skill": "Telematics analytics", "level": "Intermediate"
        },
        {
            "q": "What SQL query structure is used to find the top 5 vehicles by energy consumption last month?",
            "options": {"A": "SELECT * FROM vehicles", "B": "SELECT vehicle_id, SUM(energy_kwh) FROM sessions WHERE month = last_month GROUP BY vehicle_id ORDER BY 2 DESC LIMIT 5", "C": "UPDATE vehicles SET rank = 1", "D": "DELETE FROM low_consumption"},
            "answer": "B", "skill": "SQL", "level": "Intermediate"
        },
        {
            "q": "What is the purpose of a heartbeat signal from a telematics device?",
            "options": {"A": "Measure heart rate of the driver", "B": "Periodic signal confirming the device is online and communicating with the backend", "C": "Trigger charging session", "D": "Reset the ECU"},
            "answer": "B", "skill": "Telematics", "level": "Beginner"
        },
    ],

    "EV Telematics Developer": [
        {
            "q": "What is the function of an OBD-II (On-Board Diagnostics) port in vehicle telematics?",
            "options": {"A": "Charge the battery", "B": "Provide standardised access to vehicle ECU data including fault codes and sensor parameters", "C": "Control the infotainment system", "D": "Connect to the internet directly"},
            "answer": "B", "skill": "OBD-II", "level": "Beginner"
        },
        {
            "q": "MQTT retain flag is set when:",
            "options": {"A": "Message must be encrypted", "B": "The broker should store the last message on a topic and deliver it immediately to new subscribers", "C": "Message should be deleted immediately", "D": "QoS level is 0"},
            "answer": "B", "skill": "MQTT", "level": "Advanced"
        },
        {
            "q": "In a telematics device, edge computing processes data locally before sending to cloud primarily to:",
            "options": {"A": "Reduce device battery life", "B": "Reduce cellular data usage and latency by filtering and pre-processing data on-device", "C": "Increase raw data volume sent to cloud", "D": "Replace the cloud entirely"},
            "answer": "B", "skill": "Edge computing", "level": "Intermediate"
        },
        {
            "q": "LTE Cat-M1 (LTE-M) is preferred for EV telematics over standard LTE because:",
            "options": {"A": "It supports higher data rates", "B": "It offers lower power consumption and better coverage in weak signal areas at lower module cost", "C": "It is faster than 5G", "D": "It eliminates the need for SIM cards"},
            "answer": "B", "skill": "LTE/5G", "level": "Intermediate"
        },
        {
            "q": "FOTA (Firmware Over the Air) update rollback is triggered when:",
            "options": {"A": "Update downloads successfully", "B": "The new firmware fails integrity check or causes device instability, restoring the previous version", "C": "Battery is full", "D": "User requests rollback manually only"},
            "answer": "B", "skill": "FOTA", "level": "Advanced"
        },
    ],

    "EV Energy Storage Analyst": [
        {
            "q": "What does HOMER Pro software optimise in an EV charging + storage hybrid system?",
            "options": {"A": "BMS parameters", "B": "Sizing of solar PV, battery storage, and grid connection to minimise cost and meet load demand", "C": "Motor control algorithms", "D": "OCPP backend design"},
            "answer": "B", "skill": "Energy storage sizing", "level": "Intermediate"
        },
        {
            "q": "Round-trip efficiency (RTE) of a battery energy storage system is defined as:",
            "options": {"A": "Energy in / energy out of the charger", "B": "Energy discharged / energy charged, accounting for losses in both charge and discharge cycles", "C": "Distance travelled per kWh", "D": "Charge time / discharge time"},
            "answer": "B", "skill": "Energy modeling", "level": "Intermediate"
        },
        {
            "q": "Peak shaving using a battery storage system at a charging hub reduces:",
            "options": {"A": "Total energy consumed", "B": "The peak demand drawn from the grid, lowering utility demand charges", "C": "Number of vehicles charged", "D": "Battery capacity over time"},
            "answer": "B", "skill": "Grid integration", "level": "Intermediate"
        },
        {
            "q": "What is the levelised cost of storage (LCOS)?",
            "options": {"A": "Purchase price of the battery", "B": "Total life cycle cost of the storage system per kWh of energy delivered over its lifetime", "C": "Annual maintenance cost", "D": "Cost per charging session"},
            "answer": "B", "skill": "Energy economics", "level": "Advanced"
        },
        {
            "q": "Frequency regulation as a grid service from EV batteries involves:",
            "options": {"A": "Adjusting AC supply frequency manually", "B": "Rapidly charging/discharging to balance grid frequency deviations in real time", "C": "Replacing grid frequency meters", "D": "Providing reactive power only"},
            "answer": "B", "skill": "Grid services", "level": "Advanced"
        },
    ],

    "EV Renewable Integration Specialist": [
        {
            "q": "What is curtailment in the context of solar + EV charging integration?",
            "options": {"A": "Cutting cable during installation", "B": "Reducing solar generation output when supply exceeds grid capacity or local demand", "C": "Limiting EV battery charging rate", "D": "Reducing inverter efficiency"},
            "answer": "B", "skill": "Grid integration", "level": "Intermediate"
        },
        {
            "q": "Smart charging with renewable energy uses what strategy to maximise solar self-consumption?",
            "options": {"A": "Always charge at maximum rate", "B": "Schedule EV charging during peak solar generation hours and reduce charging when solar is low", "C": "Charge only at night", "D": "Avoid charging on sunny days"},
            "answer": "B", "skill": "Demand response", "level": "Intermediate"
        },
        {
            "q": "What is a grid code and why must EV charging systems comply with it?",
            "options": {"A": "Software licensing code", "B": "Technical standards mandated by grid operators defining connection, protection, and power quality requirements", "C": "Charging connector standard", "D": "OCPP version"},
            "answer": "B", "skill": "Grid codes", "level": "Intermediate"
        },
        {
            "q": "SCADA systems in a renewable + EV hub provide:",
            "options": {"A": "Driver navigation", "B": "Supervisory control and real-time monitoring of energy flows, solar output, and storage status", "C": "Battery chemistry analysis", "D": "OCPP message routing"},
            "answer": "B", "skill": "SCADA", "level": "Intermediate"
        },
        {
            "q": "Power Purchase Agreement (PPA) in the context of an EV fleet operator means:",
            "options": {"A": "Buying EV vehicles in bulk", "B": "Contracting to buy renewable electricity at a fixed price directly from a generator, reducing exposure to market rates", "C": "Purchasing charging hardware", "D": "Signing OCPP service contract"},
            "answer": "B", "skill": "Energy procurement", "level": "Advanced"
        },
    ],

    # =========================================================================
    # CYBERSECURITY
    # =========================================================================

    "EV Cybersecurity Specialist": [
        {
            "q": "What does TARA (Threat Analysis and Risk Assessment) produce in ISO 21434?",
            "options": {"A": "Battery test report", "B": "Identification of cybersecurity threats, their risk levels, and required security goals for a vehicle system", "C": "Software architecture document", "D": "Quality audit report"},
            "answer": "B", "skill": "TARA", "level": "Advanced"
        },
        {
            "q": "What is the UNECE WP.29 R155 regulation?",
            "options": {"A": "Battery recycling standard", "B": "Mandatory cybersecurity management system requirement for vehicle type approval in UN member countries", "C": "Charging connector standard", "D": "Autonomous driving safety standard"},
            "answer": "B", "skill": "Automotive cybersecurity", "level": "Advanced"
        },
        {
            "q": "In CAN bus security, what is a replay attack?",
            "options": {"A": "Watching a video twice", "B": "Capturing legitimate CAN messages and replaying them to trigger unauthorised vehicle actions", "C": "Overloading the CAN bus", "D": "Injecting random data"},
            "answer": "B", "skill": "CAN security", "level": "Intermediate"
        },
        {
            "q": "PKI (Public Key Infrastructure) in V2X communication is used to:",
            "options": {"A": "Encrypt video streams", "B": "Issue digital certificates to vehicles for authenticating V2X messages and preventing spoofing", "C": "Store firmware updates", "D": "Manage OCPP sessions"},
            "answer": "B", "skill": "PKI", "level": "Advanced"
        },
        {
            "q": "OWASP Top 10 is relevant to EV charging backend APIs primarily for:",
            "options": {"A": "Hardware design guidance", "B": "Identifying the most critical web application security risks like injection, broken auth, and misconfigurations", "C": "Battery management", "D": "Motor control"},
            "answer": "B", "skill": "OWASP", "level": "Intermediate"
        },
    ],

    "EV Cloud Security Analyst": [
        {
            "q": "What is the principle of least privilege in cloud IAM?",
            "options": {"A": "Give all users admin rights", "B": "Grant only the minimum permissions necessary for a user or service to perform its function", "C": "Restrict access to developers only", "D": "Use shared credentials"},
            "answer": "B", "skill": "IAM", "level": "Intermediate"
        },
        {
            "q": "Zero trust architecture assumes:",
            "options": {"A": "Internal network is always safe", "B": "No user or device is trusted by default, even inside the network — verify every request explicitly", "C": "Firewalls provide complete protection", "D": "VPN is sufficient security"},
            "answer": "B", "skill": "Zero trust", "level": "Intermediate"
        },
        {
            "q": "What does a cloud SIEM do with log data?",
            "options": {"A": "Archive logs to cold storage", "B": "Correlate events across services in real time to detect security incidents and generate alerts", "C": "Delete old logs automatically", "D": "Compress logs for storage"},
            "answer": "B", "skill": "SIEM", "level": "Intermediate"
        },
        {
            "q": "SOC 2 Type II audit reports on:",
            "options": {"A": "Financial statements", "B": "Effectiveness of a service organisation's security controls over a period of time (typically 6–12 months)", "C": "Environmental compliance", "D": "Hardware manufacturing quality"},
            "answer": "B", "skill": "Compliance", "level": "Advanced"
        },
        {
            "q": "AWS GuardDuty is a service that provides:",
            "options": {"A": "Virtual firewall rules", "B": "Intelligent threat detection using ML to identify suspicious activity in AWS accounts", "C": "Identity management", "D": "Object storage encryption"},
            "answer": "B", "skill": "AWS security", "level": "Intermediate"
        },
    ],

    # =========================================================================
    # QUALITY, RELIABILITY & TESTING
    # =========================================================================

    "EV Quality Assurance Specialist": [
        {
            "q": "What does IATF 16949 add to ISO 9001 for the automotive industry?",
            "options": {"A": "Environmental management requirements", "B": "Automotive-specific requirements including APQP, PPAP, FMEA, MSA, and SPC", "C": "Financial audit requirements", "D": "IT security standards"},
            "answer": "B", "skill": "IATF 16949", "level": "Advanced"
        },
        {
            "q": "In a PPAP submission, what is a PSW (Part Submission Warrant)?",
            "options": {"A": "Payment invoice", "B": "Document signed by supplier confirming all PPAP elements are complete and product meets requirements", "C": "Production schedule", "D": "Engineering drawing"},
            "answer": "B", "skill": "PPAP", "level": "Intermediate"
        },
        {
            "q": "APQP Phase 3 (Process Design and Development) produces which key output?",
            "options": {"A": "Customer requirements", "B": "Process flow diagrams, PFMEA, control plan, and work instructions", "C": "Financial projections", "D": "Product design"},
            "answer": "B", "skill": "APQP", "level": "Advanced"
        },
        {
            "q": "SPC (Statistical Process Control) uses control charts to:",
            "options": {"A": "Set production targets", "B": "Monitor process variation over time and detect special cause (out-of-control) events", "C": "Calculate profit margins", "D": "Manage employee performance"},
            "answer": "B", "skill": "SPC", "level": "Intermediate"
        },
        {
            "q": "What does MSA (Measurement System Analysis) validate?",
            "options": {"A": "Marketing strategy accuracy", "B": "That a measurement system (gauge, instrument, operator) is capable of producing consistent and accurate results", "C": "Software module quality", "D": "Machine speed"},
            "answer": "B", "skill": "MSA", "level": "Intermediate"
        },
    ],

    "EV Reliability Engineer": [
        {
            "q": "A bathtub curve in reliability engineering shows failure rates over time with three regions. What does the middle (flat) region represent?",
            "options": {"A": "Infant mortality (early failures)", "B": "Useful life — random failures at a constant, low rate", "C": "Wear-out phase", "D": "Design phase"},
            "answer": "B", "skill": "Reliability theory", "level": "Intermediate"
        },
        {
            "q": "What is Design for Reliability (DfR) and when in the product lifecycle is it applied?",
            "options": {"A": "Testing reliability after manufacturing; end of life", "B": "Engineering activities during design phase to proactively identify and mitigate failure modes before production", "C": "Field service repair manual", "D": "Customer warranty policy"},
            "answer": "B", "skill": "DfR", "level": "Intermediate"
        },
        {
            "q": "Accelerated Life Testing (ALT) stresses a component beyond normal conditions to:",
            "options": {"A": "Destroy the component for safety", "B": "Quickly accumulate equivalent field exposure and predict real-world reliability in compressed time", "C": "Improve manufacturing yield", "D": "Validate software"},
            "answer": "B", "skill": "ALT", "level": "Advanced"
        },
        {
            "q": "HALT (Highly Accelerated Life Testing) is exploratory, meaning:",
            "options": {"A": "It tests to specification limits only", "B": "It pushes beyond specification to find design weaknesses not revealed by standard tests", "C": "It is done in production only", "D": "It measures mean time between failures"},
            "answer": "B", "skill": "HALT", "level": "Advanced"
        },
        {
            "q": "In Weibull analysis, if β = 1, what does this indicate about the failure distribution?",
            "options": {"A": "Increasing failure rate (wear-out)", "B": "Constant failure rate (exponential distribution — random failures)", "C": "Decreasing failure rate (early life)", "D": "Bi-modal failure distribution"},
            "answer": "B", "skill": "Weibull analysis", "level": "Advanced"
        },
    ],

    "EV Test Lab Coordinator": [
        {
            "q": "Equipment calibration in a test lab must be traceable to:",
            "options": {"A": "The company's internal standard", "B": "National or international standards (e.g., NABL-accredited / ISO 17025 calibration)", "C": "The last test result", "D": "Manufacturer specifications only"},
            "answer": "B", "skill": "Calibration", "level": "Intermediate"
        },
        {
            "q": "What does a DVP&R (Design Verification Plan and Report) document?",
            "options": {"A": "Employee performance", "B": "All tests planned to verify design requirements, with results documented to demonstrate compliance", "C": "Manufacturing process steps", "D": "Customer pricing"},
            "answer": "B", "skill": "Test planning", "level": "Intermediate"
        },
        {
            "q": "LabVIEW's graphical programming paradigm is called:",
            "options": {"A": "Object-oriented programming", "B": "Dataflow programming — execution is determined by the flow of data between nodes", "C": "Procedural programming", "D": "Functional programming"},
            "answer": "B", "skill": "LabVIEW", "level": "Intermediate"
        },
        {
            "q": "Requirements traceability matrix (RTM) links:",
            "options": {"A": "Employees to projects", "B": "Each requirement to its corresponding test cases to ensure complete test coverage", "C": "Parts to suppliers", "D": "Software to hardware"},
            "answer": "B", "skill": "Traceability", "level": "Intermediate"
        },
        {
            "q": "When ECU flashing in a test lab, what must be verified before flashing begins?",
            "options": {"A": "Room temperature", "B": "Correct software version, stable power supply voltage, and that no other processes are communicating with the ECU", "C": "Lab WiFi connection", "D": "Number of test engineers present"},
            "answer": "B", "skill": "ECU flashing", "level": "Intermediate"
        },
    ],

    "EV Quality Inspector": [
        {
            "q": "AQL (Acceptable Quality Level) sampling in incoming inspection defines:",
            "options": {"A": "100% inspection of all parts", "B": "Statistical sampling plan where AQL specifies the maximum acceptable defect rate for a lot to be accepted", "C": "Quality of the assembly process", "D": "Supplier payment terms"},
            "answer": "B", "skill": "AQL sampling", "level": "Intermediate"
        },
        {
            "q": "GD&T datum references are used to:",
            "options": {"A": "Measure surface roughness", "B": "Establish a coordinate system from which part geometry is measured to ensure consistent inspection", "C": "Specify material hardness", "D": "Define colour tolerances"},
            "answer": "B", "skill": "GD&T", "level": "Intermediate"
        },
        {
            "q": "A gauge R&R study evaluates:",
            "options": {"A": "Production output rate", "B": "Repeatability (same operator, same gauge) and reproducibility (different operators) of a measurement system", "C": "Gauge battery life", "D": "Number of defective parts"},
            "answer": "B", "skill": "Gauge R&R", "level": "Advanced"
        },
        {
            "q": "What does a non-conformance report (NCR) trigger in a quality system?",
            "options": {"A": "Payment to supplier", "B": "Formal documentation, segregation of non-conforming material, and root cause analysis / corrective action", "C": "Production ramp-up", "D": "Customer delivery"},
            "answer": "B", "skill": "Quality management", "level": "Intermediate"
        },
        {
            "q": "Functional testing of an EV battery module in a quality lab verifies:",
            "options": {"A": "Module weight", "B": "Electrical performance (capacity, IR, voltage) meets specification before assembly into the pack", "C": "Module colour", "D": "Packaging integrity only"},
            "answer": "B", "skill": "Functional testing", "level": "Beginner"
        },
    ],

    "EV Component Validation Engineer": [
        {
            "q": "What is the DVP (Design Verification Plan)?",
            "options": {"A": "Document describing vehicle features", "B": "Plan specifying all tests required to verify component design meets engineering requirements", "C": "Daily vehicle performance log", "D": "Driver training plan"},
            "answer": "B", "skill": "V&V testing", "level": "Intermediate"
        },
        {
            "q": "IP67 rating on an EV component means it is protected against:",
            "options": {"A": "Electromagnetic interference", "B": "Dust ingress (6) and temporary immersion in water up to 1m for 30 minutes (7)", "C": "Vibration only", "D": "High temperature"},
            "answer": "B", "skill": "Environmental testing", "level": "Intermediate"
        },
        {
            "q": "EMC pre-compliance testing is performed to:",
            "options": {"A": "Obtain final CE certification", "B": "Identify potential EMI issues early in development, before costly formal accredited lab testing", "C": "Measure battery capacity", "D": "Validate OCPP communication"},
            "answer": "B", "skill": "EMC testing", "level": "Intermediate"
        },
        {
            "q": "A vibration test profile for an automotive component is derived from:",
            "options": {"A": "Designer's preference", "B": "Field-measured vibration data from the vehicle's installation location (PSD profile)", "C": "Component weight", "D": "Supplier recommendation"},
            "answer": "B", "skill": "Vibration testing", "level": "Advanced"
        },
        {
            "q": "What does thermal cycling validation test on an EV power electronics module?",
            "options": {"A": "Maximum charging rate", "B": "Resistance of solder joints and encapsulation to repeated thermal expansion/contraction over many cycles", "C": "Software stability", "D": "Chemical compatibility"},
            "answer": "B", "skill": "Thermal testing", "level": "Advanced"
        },
    ],

    "EV Electronics Test Engineer": [
        {
            "q": "What does a spectrum analyser measure that a standard oscilloscope cannot directly display?",
            "options": {"A": "Voltage amplitude over time", "B": "Signal power distribution across a frequency range (frequency domain)", "C": "Current waveform", "D": "Phase angle between signals"},
            "answer": "B", "skill": "Test equipment", "level": "Intermediate"
        },
        {
            "q": "When testing a PCB with a logic analyser, what data is captured?",
            "options": {"A": "Analog voltage levels", "B": "Digital signal states over time, enabling decoding of protocols like CAN, SPI, I2C", "C": "Component temperatures", "D": "Power consumption"},
            "answer": "B", "skill": "Logic analyser", "level": "Intermediate"
        },
        {
            "q": "Boundary scan (JTAG) testing on a PCB allows testing of:",
            "options": {"A": "Thermal characteristics", "B": "Interconnections between ICs and board functionality without physical test probes using built-in boundary scan cells", "C": "RF emissions", "D": "Firmware execution speed"},
            "answer": "B", "skill": "JTAG", "level": "Advanced"
        },
        {
            "q": "Signal integrity analysis identifies which PCB design issues?",
            "options": {"A": "Component cost", "B": "Reflections, crosstalk, ground bounce, and impedance mismatch causing signal degradation", "C": "BOM errors", "D": "Solder quality"},
            "answer": "B", "skill": "Signal integrity", "level": "Advanced"
        },
        {
            "q": "A power supply rejection ratio (PSRR) test on an LDO regulator measures:",
            "options": {"A": "Output current capability", "B": "How well the regulator attenuates supply noise and prevents it from appearing on the output", "C": "Thermal shutdown threshold", "D": "Input voltage range"},
            "answer": "B", "skill": "Power electronics testing", "level": "Advanced"
        },
    ],

    "EV Hardware Debug Engineer": [
        {
            "q": "When probing a suspected faulty solder joint on an IGBT driver circuit, which technique applies a small current to identify high-resistance connections?",
            "options": {"A": "Oscilloscope voltage probe", "B": "Kelvin (4-wire) resistance measurement with a milliohmmeter", "C": "Continuity buzzer only", "D": "Visual inspection with microscope"},
            "answer": "B", "skill": "Lab debugging", "level": "Advanced"
        },
        {
            "q": "Thermal imaging in hardware debug helps identify:",
            "options": {"A": "Software bugs", "B": "Overheating components due to excessive power dissipation, poor solder joints, or inadequate heatsinking", "C": "Memory leaks", "D": "EMC failures"},
            "answer": "B", "skill": "Thermal imaging", "level": "Intermediate"
        },
        {
            "q": "When a microcontroller enters a hard fault exception, the first debug step is:",
            "options": {"A": "Replace the microcontroller", "B": "Examine the stack trace and fault status registers (e.g., CFSR, BFAR) via JTAG debugger to identify the cause", "C": "Recompile the code", "D": "Reset the board repeatedly"},
            "answer": "B", "skill": "Embedded debugging", "level": "Advanced"
        },
        {
            "q": "What is a flying probe test in PCB manufacturing?",
            "options": {"A": "Drone-based inspection", "B": "Automated electrical test using moving probes to test connections without a dedicated fixture", "C": "Optical inspection by robot", "D": "X-ray inspection"},
            "answer": "B", "skill": "PCB testing", "level": "Intermediate"
        },
        {
            "q": "Schematic review during hardware debug is important because:",
            "options": {"A": "It replaces physical testing", "B": "It can reveal design errors (wrong component values, missing pull-ups, incorrect net connections) before extensive lab debugging", "C": "It is mandated by ISO 26262", "D": "It measures signal frequencies"},
            "answer": "B", "skill": "Schematic reading", "level": "Beginner"
        },
    ],

    # =========================================================================
    # REGULATORY, SAFETY & STANDARDS
    # =========================================================================

    "EV Safety Engineer": [
        {
            "q": "In ISO 26262 HARA, what does ASIL stand for?",
            "options": {"A": "Automotive System Integration Level", "B": "Automotive Safety Integrity Level — risk classification from A (lowest) to D (highest)", "C": "Automated Safety Inspection Limit", "D": "Assembly Safety Instruction Level"},
            "answer": "B", "skill": "ISO 26262", "level": "Intermediate"
        },
        {
            "q": "SOTIF (ISO 21448) addresses safety risks that arise from:",
            "options": {"A": "Random hardware failures", "B": "Functional insufficiencies in intended functionality (e.g., ADAS sensor limitations) without hardware faults", "C": "Cybersecurity attacks", "D": "Manufacturing defects"},
            "answer": "B", "skill": "SOTIF", "level": "Advanced"
        },
        {
            "q": "An ASIL decomposition from ASIL D to ASIL B + ASIL B requires:",
            "options": {"A": "Two identical hardware channels", "B": "Two sufficiently independent channels each meeting ASIL B, together achieving equivalent ASIL D coverage", "C": "One channel with redundancy", "D": "Software-only implementation"},
            "answer": "B", "skill": "ASIL decomposition", "level": "Advanced"
        },
        {
            "q": "What is a safety case in ISO 26262?",
            "options": {"A": "Physical protective case for the ECU", "B": "Structured argument with evidence that a system achieves its safety goals and is acceptably safe for the intended use", "C": "Emergency shut-off procedure", "D": "Legal liability document"},
            "answer": "B", "skill": "Safety case", "level": "Intermediate"
        },
        {
            "q": "In a fault tree analysis (FTA), an OR gate at the top event means:",
            "options": {"A": "All basic events must occur for the top event", "B": "Any single basic event (failure) can independently cause the top (undesired) event", "C": "The top event is impossible", "D": "Multiple events must fail simultaneously only"},
            "answer": "B", "skill": "Fault tree analysis", "level": "Intermediate"
        },
    ],

    "EV Regulatory Compliance Expert": [
        {
            "q": "What does AIS-138 govern in India?",
            "options": {"A": "EV motor efficiency", "B": "EV supply equipment (EVSE) safety and performance requirements in India", "C": "Battery chemistry", "D": "Autonomous driving regulations"},
            "answer": "B", "skill": "AIS standards", "level": "Intermediate"
        },
        {
            "q": "WLTP (Worldwide harmonised Light vehicles Test Procedure) is used to measure:",
            "options": {"A": "Battery manufacturing quality", "B": "Standardised vehicle energy consumption and emissions / range under a representative real-world driving cycle", "C": "Charging speed", "D": "Motor torque output"},
            "answer": "B", "skill": "WLTP", "level": "Intermediate"
        },
        {
            "q": "Type approval for an EV in India requires submission to which authority?",
            "options": {"A": "RBI", "B": "ARAI or ICAT (testing agencies under MoRTH) for vehicle type approval before commercial sale", "C": "SEBI", "D": "IRDAI"},
            "answer": "B", "skill": "Homologation", "level": "Intermediate"
        },
        {
            "q": "UNECE Regulation 100 (R100) covers:",
            "options": {"A": "Autonomous driving level requirements", "B": "Safety requirements for the propulsion battery system of electric vehicles", "C": "Charging protocol standards", "D": "EV noise emission limits"},
            "answer": "B", "skill": "UNECE standards", "level": "Advanced"
        },
        {
            "q": "CE marking on an EV charger sold in the European Union indicates:",
            "options": {"A": "Chinese Export certification", "B": "The product meets EU health, safety, and environmental protection requirements for market access", "C": "Carbon emission compliance", "D": "Consumer Electronics standard"},
            "answer": "B", "skill": "CE marking", "level": "Beginner"
        },
    ],

    "EV Regulatory Affairs Specialist": [
        {
            "q": "CMVR (Central Motor Vehicles Rules) in India is enforced by:",
            "options": {"A": "SEBI", "B": "Ministry of Road Transport and Highways (MoRTH)", "C": "Ministry of Power", "D": "NITI Aayog"},
            "answer": "B", "skill": "CMVR", "level": "Beginner"
        },
        {
            "q": "What does a Technical Dossier in a vehicle type approval submission contain?",
            "options": {"A": "Marketing brochure", "B": "Detailed technical specifications, test reports, drawings, and declarations proving regulatory compliance", "C": "Financial projections", "D": "Dealer network information"},
            "answer": "B", "skill": "Technical documentation", "level": "Intermediate"
        },
        {
            "q": "PLI (Production Linked Incentive) scheme for Advanced Chemistry Cell batteries in India aims to:",
            "options": {"A": "Import more batteries", "B": "Incentivise domestic manufacturing of advanced battery cells by offering financial incentives based on production output", "C": "Ban foreign battery imports", "D": "Standardise battery chemistry"},
            "answer": "B", "skill": "PLI scheme", "level": "Intermediate"
        },
        {
            "q": "FAME II (Faster Adoption and Manufacturing of Hybrid and EV) scheme supports:",
            "options": {"A": "Fuel cell vehicles only", "B": "Purchase of electric vehicles and charging infrastructure development through demand incentives and capital subsidies", "C": "ICE vehicle export", "D": "Battery recycling only"},
            "answer": "B", "skill": "FAME II", "level": "Beginner"
        },
        {
            "q": "An emission norm waiver for EVs under BS6 regulations in India means:",
            "options": {"A": "EVs must still comply with tailpipe limits", "B": "Zero-emission EVs are exempt from tailpipe emission norms since they produce no exhaust", "C": "EVs follow older BS4 norms", "D": "EVs must comply with a separate stricter standard"},
            "answer": "B", "skill": "Emission norms", "level": "Intermediate"
        },
    ],

    "EV Safety Trainer": [
        {
            "q": "When responding to an EV involved in a road accident, first responders should:",
            "options": {"A": "Immediately try to charge the battery", "B": "Identify the vehicle as EV, locate the service disconnect, and assume HV system is live until confirmed otherwise", "C": "Open the hood immediately", "D": "Tow the vehicle without precautions"},
            "answer": "B", "skill": "EV rescue", "level": "Intermediate"
        },
        {
            "q": "Class D fire extinguisher is used for:",
            "options": {"A": "Electrical fires", "B": "Metal fires (lithium and other reactive metals)", "C": "Flammable liquid fires", "D": "Gas fires"},
            "answer": "B", "skill": "Battery fire response", "level": "Intermediate"
        },
        {
            "q": "The ADDIE instructional design model stands for:",
            "options": {"A": "Assess, Design, Deliver, Improve, Evaluate", "B": "Analysis, Design, Development, Implementation, Evaluation", "C": "Apply, Develop, Deploy, Integrate, Execute", "D": "Aim, Draft, Design, Implement, Examine"},
            "answer": "B", "skill": "Instructional design", "level": "Intermediate"
        },
        {
            "q": "PPE required for high-voltage EV battery work (>60V DC) must include insulated gloves rated to at minimum:",
            "options": {"A": "Class 00 (500V AC)", "B": "Class 0 (1000V AC / 1500V DC) or higher depending on system voltage", "C": "Rubber gloves with no rating", "D": "Standard work gloves"},
            "answer": "B", "skill": "HV safety", "level": "Intermediate"
        },
        {
            "q": "What does a Kirkpatrick Level 3 training evaluation measure?",
            "options": {"A": "Trainee satisfaction with the course", "B": "On-the-job behaviour change — whether trainees are applying the learning in their work", "C": "Knowledge gained immediately after training", "D": "Business results"},
            "answer": "B", "skill": "Training evaluation", "level": "Advanced"
        },
    ],

    "EV Site Safety Inspector": [
        {
            "q": "OSHA's General Duty Clause requires employers to:",
            "options": {"A": "Provide free meals", "B": "Provide a workplace free from recognised hazards that are causing or likely to cause death or serious physical harm", "C": "Install CCTV cameras", "D": "Conduct annual salary reviews"},
            "answer": "B", "skill": "OSHA", "level": "Beginner"
        },
        {
            "q": "An incident investigation using the '5 Whys' technique aims to find:",
            "options": {"A": "Who is at fault", "B": "Root cause by repeatedly asking 'why' until the underlying systemic cause is identified", "C": "The cost of the incident", "D": "The number of incidents"},
            "answer": "B", "skill": "Incident investigation", "level": "Intermediate"
        },
        {
            "q": "A Permit to Work (PTW) system ensures:",
            "options": {"A": "Workers are paid on time", "B": "Hazardous work is formally authorised, risks are assessed, and controls are in place before work begins", "C": "Project is on schedule", "D": "Quality of materials used"},
            "answer": "B", "skill": "Permit to Work", "level": "Intermediate"
        },
        {
            "q": "Arc flash PPE selection is based on which calculation?",
            "options": {"A": "Cable length", "B": "Incident energy analysis (in cal/cm²) determining the energy at a working distance during an arc flash event", "C": "Ambient temperature", "D": "Charger brand"},
            "answer": "B", "skill": "Arc flash safety", "level": "Advanced"
        },
        {
            "q": "What is the purpose of a toolbox talk (TBT) before starting work?",
            "options": {"A": "Distribute tools to workers", "B": "Brief safety meeting to discuss specific hazards, controls, and safe procedures for the day's tasks", "C": "Review project financials", "D": "Plan lunch breaks"},
            "answer": "B", "skill": "Safety management", "level": "Beginner"
        },
    ],

    "EV Infrastructure Policy Advisor": [
        {
            "q": "FAME II scheme in India provides demand incentives for EVs based on:",
            "options": {"A": "Vehicle colour", "B": "Battery capacity (kWh) and vehicle type, with higher incentives for public transport and 3-wheelers", "C": "Manufacturer's revenue", "D": "Driver's income level"},
            "answer": "B", "skill": "FAME II", "level": "Intermediate"
        },
        {
            "q": "What is a key barrier to EV adoption in Tier-2 and Tier-3 cities in India that policy must address?",
            "options": {"A": "Too many EVs already", "B": "Lack of public charging infrastructure, range anxiety, and higher upfront vehicle cost without adequate financing", "C": "Traffic congestion only", "D": "Surplus battery supply"},
            "answer": "B", "skill": "EV policy", "level": "Beginner"
        },
        {
            "q": "Carbon credit markets allow EV fleet operators to:",
            "options": {"A": "Sell carbon emissions", "B": "Generate and sell verified emission reduction credits by operating zero-emission EVs instead of ICE vehicles", "C": "Buy carbon offsets only", "D": "Avoid all taxes"},
            "answer": "B", "skill": "Sustainability policy", "level": "Advanced"
        },
        {
            "q": "The National Electric Mobility Mission Plan (NEMMP) in India targeted how many EVs by 2020?",
            "options": {"A": "500,000", "B": "6–7 million EVs on Indian roads by 2020", "C": "10 million", "D": "100,000"},
            "answer": "B", "skill": "EV policy", "level": "Intermediate"
        },
        {
            "q": "What does interoperability mean in the context of EV charging policy?",
            "options": {"A": "Vehicles from one brand only charge at one brand's charger", "B": "Any EV can charge at any compliant charger regardless of brand, using open protocols like OCPP and OCPI", "C": "Chargers must match vehicle colour", "D": "Charging speed must be identical across all chargers"},
            "answer": "B", "skill": "Charging policy", "level": "Intermediate"
        },
    ],

    # =========================================================================
    # MECHANICAL, MATERIALS & THERMAL
    # =========================================================================

    "EV Mechanical Design Engineer": [
        {
            "q": "What does DFMEA (Design Failure Mode and Effects Analysis) identify?",
            "options": {"A": "Manufacturing defects only", "B": "Potential failure modes in a design and their effects on system function, used to improve design before release", "C": "Customer complaints", "D": "Supply chain risks"},
            "answer": "B", "skill": "DFMEA", "level": "Intermediate"
        },
        {
            "q": "FEA (Finite Element Analysis) in SolidWorks Simulation is used for:",
            "options": {"A": "Creating 2D drawings", "B": "Predicting stress, strain, deformation, and fatigue in components under applied loads", "C": "Generating bill of materials", "D": "Writing software code"},
            "answer": "B", "skill": "FEA", "level": "Intermediate"
        },
        {
            "q": "GD&T True Position tolerance controls:",
            "options": {"A": "Surface roughness", "B": "The location of a feature (e.g., hole centre) relative to a datum reference frame", "C": "Material hardness", "D": "Thread pitch"},
            "answer": "B", "skill": "GD&T", "level": "Intermediate"
        },
        {
            "q": "In CATIA V5, an Assembly Design workbench is used to:",
            "options": {"A": "Create 2D engineering drawings", "B": "Position, constrain, and manage relationships between individual part bodies in an assembly", "C": "Run FEA analysis", "D": "Write macros"},
            "answer": "B", "skill": "CATIA", "level": "Intermediate"
        },
        {
            "q": "What is DFM (Design for Manufacturability) and why is it important in EV component design?",
            "options": {"A": "Designing for maximum performance only", "B": "Designing components to be easily and cost-effectively manufactured, reducing production complexity, scrap, and assembly errors", "C": "Designing the factory layout", "D": "Documenting the design"},
            "answer": "B", "skill": "DFM", "level": "Intermediate"
        },
    ],

    "EV Materials Specialist": [
        {
            "q": "Why are carbon fibre reinforced polymers (CFRP) used in EV structural components?",
            "options": {"A": "They are cheap", "B": "Exceptional strength-to-weight ratio reduces vehicle mass, improving range and handling", "C": "They conduct electricity well", "D": "They are easy to recycle"},
            "answer": "B", "skill": "Composites", "level": "Intermediate"
        },
        {
            "q": "CES EduPack (Granta) is used in materials selection for:",
            "options": {"A": "Writing material specifications", "B": "Comparing material properties using Ashby charts and selecting optimal materials for performance, cost, and sustainability", "C": "Ordering materials from suppliers", "D": "Performing FEA analysis"},
            "answer": "B", "skill": "CES EduPack", "level": "Intermediate"
        },
        {
            "q": "Galvanic corrosion in an EV battery tray occurs when:",
            "options": {"A": "Temperature exceeds 80°C", "B": "Two dissimilar metals (e.g., aluminium tray and steel fastener) are in contact in the presence of an electrolyte", "C": "Battery is overcharged", "D": "Cell voltage drops below 2V"},
            "answer": "B", "skill": "Corrosion engineering", "level": "Advanced"
        },
        {
            "q": "Life Cycle Assessment (LCA) of an EV battery evaluates environmental impact across:",
            "options": {"A": "Manufacturing phase only", "B": "Entire life from raw material extraction, manufacturing, use, and end-of-life (cradle-to-grave)", "C": "Use phase only", "D": "Recycling phase only"},
            "answer": "B", "skill": "LCA", "level": "Intermediate"
        },
        {
            "q": "ASTM standards in materials testing define:",
            "options": {"A": "Software quality requirements", "B": "Standardised test methods and material specifications ensuring reproducibility and comparison across labs", "C": "Building codes", "D": "Vehicle emission limits"},
            "answer": "B", "skill": "ASTM standards", "level": "Beginner"
        },
    ],

    "EV Materials R&D Scientist": [
        {
            "q": "XRD (X-ray Diffraction) analysis of a battery cathode material reveals:",
            "options": {"A": "Surface morphology", "B": "Crystal structure, phase composition, and lattice parameter changes due to cycling or synthesis conditions", "C": "Particle size distribution", "D": "Elemental mass percentage"},
            "answer": "B", "skill": "XRD", "level": "Advanced"
        },
        {
            "q": "What is the main function of the electrolyte in a lithium-ion battery?",
            "options": {"A": "Conduct electrons between electrodes", "B": "Provide ionic conductivity (Li+ transport) between anode and cathode while being electronically insulating", "C": "Store energy mechanically", "D": "Prevent thermal expansion"},
            "answer": "B", "skill": "Electrolyte chemistry", "level": "Intermediate"
        },
        {
            "q": "Silicon anode materials offer higher capacity than graphite but suffer from:",
            "options": {"A": "Poor electronic conductivity", "B": "Large volume expansion (~300%) during lithiation causing mechanical degradation and capacity fade", "C": "Low lithium insertion voltage", "D": "High cost only"},
            "answer": "B", "skill": "Anode materials", "level": "Advanced"
        },
        {
            "q": "SEM (Scanning Electron Microscopy) is used in battery research to:",
            "options": {"A": "Measure ionic conductivity", "B": "Visualise electrode morphology, particle distribution, and surface/interface changes at nanoscale", "C": "Perform electrochemical cycling", "D": "Calculate theoretical capacity"},
            "answer": "B", "skill": "SEM", "level": "Intermediate"
        },
        {
            "q": "What is the purpose of a separator in a lithium-ion cell?",
            "options": {"A": "Conduct lithium ions rapidly", "B": "Physically separate anode and cathode to prevent short circuit while allowing ionic transport through micropores", "C": "Store excess lithium", "D": "Provide structural support for the cell"},
            "answer": "B", "skill": "Cell components", "level": "Beginner"
        },
    ],

    "EV Hydrogen Storage Engineer": [
        {
            "q": "Type IV hydrogen storage tanks use which construction?",
            "options": {"A": "All-steel seamless vessel", "B": "Polymer (plastic) liner fully overwrapped with carbon fibre reinforced polymer (CFRP)", "C": "Aluminium liner without overwrap", "D": "Glass fibre only overwrap on steel"},
            "answer": "B", "skill": "Hydrogen storage", "level": "Advanced"
        },
        {
            "q": "Hydrogen embrittlement is a concern for high-pressure tanks because:",
            "options": {"A": "Hydrogen expands the tank", "B": "Hydrogen atoms diffuse into metal lattice reducing ductility and causing cracking under stress", "C": "Hydrogen corrodes polymer liners", "D": "Hydrogen reduces insulation"},
            "answer": "B", "skill": "Material selection", "level": "Advanced"
        },
        {
            "q": "The nominal working pressure for most automotive hydrogen fuel cell vehicles is:",
            "options": {"A": "10 bar", "B": "700 bar (70 MPa)", "C": "100 bar", "D": "350 bar only"},
            "answer": "B", "skill": "Pressure systems", "level": "Intermediate"
        },
        {
            "q": "FEM analysis on a hydrogen pressure vessel validates:",
            "options": {"A": "Thermal insulation quality", "B": "Structural integrity under burst pressure, hoop and axial stresses, and fatigue life", "C": "Hydrogen flow rate", "D": "Refuelling speed"},
            "answer": "B", "skill": "FEM analysis", "level": "Advanced"
        },
        {
            "q": "SAE J2579 standard governs:",
            "options": {"A": "EV battery testing", "B": "Technical safety requirements for fuel systems in fuel cell and other hydrogen vehicles", "C": "Charging connector design", "D": "Motor control algorithms"},
            "answer": "B", "skill": "Safety standards", "level": "Intermediate"
        },
    ],

    "EV Thermal Systems Engineer": [
        {
            "q": "A heat pump in an EV HVAC system improves range compared to resistive heating because:",
            "options": {"A": "It uses less battery power at all temperatures", "B": "COP > 1 means it moves more heat energy than the electrical energy it consumes, preserving battery range", "C": "It charges the battery simultaneously", "D": "It cools the motor instead"},
            "answer": "B", "skill": "HVAC", "level": "Intermediate"
        },
        {
            "q": "What is the role of a chiller in an integrated EV thermal management system?",
            "options": {"A": "Heat the cabin", "B": "Cool the battery or power electronics by transferring heat to the refrigerant circuit", "C": "Dehumidify the cabin only", "D": "Provide heated coolant for cabin"},
            "answer": "B", "skill": "Thermal systems", "level": "Intermediate"
        },
        {
            "q": "In ANSYS Fluent CFD, the k-ε turbulence model is selected for:",
            "options": {"A": "Laminar pipe flow", "B": "Turbulent flow regimes in cooling channels and heat exchangers to capture eddy viscosity effects", "C": "Structural stress analysis", "D": "Electromagnetic simulation"},
            "answer": "B", "skill": "CFD", "level": "Advanced"
        },
        {
            "q": "Coolant loop design in an EV must ensure:",
            "options": {"A": "Maximum coolant temperature everywhere", "B": "Uniform temperature distribution (low ΔT) across all cells/modules and adequate flow rate to remove peak heat load", "C": "No coolant flow during charging", "D": "Bypass of high-temperature cells"},
            "answer": "B", "skill": "Coolant loop design", "level": "Intermediate"
        },
        {
            "q": "What refrigerant is most commonly used in current EV heat pump systems due to low GWP?",
            "options": {"A": "R134a", "B": "R744 (CO2) or R1234yf (low GWP HFO refrigerants)", "C": "R22 (HCFC)", "D": "Ammonia (R717)"},
            "answer": "B", "skill": "Refrigerant selection", "level": "Advanced"
        },
    ],

    # =========================================================================
    # OPERATIONS, SUPPLY CHAIN & MANAGEMENT
    # =========================================================================

    "EV Supply Chain Manager": [
        {
            "q": "APQP (Advanced Product Quality Planning) is a structured process that ensures:",
            "options": {"A": "Supplier payment is on time", "B": "Product quality is planned from customer requirements through design, process planning, and production validation", "C": "Marketing campaigns are ready", "D": "Logistics routes are optimised"},
            "answer": "B", "skill": "APQP", "level": "Intermediate"
        },
        {
            "q": "What is a dual-sourcing strategy in EV battery supply chain?",
            "options": {"A": "Buying from the cheapest single supplier", "B": "Using two approved suppliers for critical materials to reduce dependency risk and ensure supply continuity", "C": "Importing from two countries", "D": "Splitting production between two factories"},
            "answer": "B", "skill": "Supplier risk management", "level": "Intermediate"
        },
        {
            "q": "S&OP (Sales and Operations Planning) in EV manufacturing aligns:",
            "options": {"A": "HR and finance teams", "B": "Demand forecasts from sales with supply capacity from operations to balance inventory and meet customer needs", "C": "Marketing and legal teams", "D": "R&D and legal teams"},
            "answer": "B", "skill": "S&OP", "level": "Intermediate"
        },
        {
            "q": "Lean manufacturing's 7 wastes (Muda) in battery pack assembly include all EXCEPT:",
            "options": {"A": "Overproduction and waiting", "B": "Innovation and R&D activities", "C": "Defects and excess inventory", "D": "Transportation and over-processing"},
            "answer": "B", "skill": "Lean manufacturing", "level": "Intermediate"
        },
        {
            "q": "SAP MM module in supply chain manages:",
            "options": {"A": "Financial reporting", "B": "Materials management including purchasing, inventory, goods receipt, and invoice verification", "C": "HR payroll", "D": "Customer relationship management"},
            "answer": "B", "skill": "SAP", "level": "Beginner"
        },
    ],

    "EV Supply Chain Analyst": [
        {
            "q": "What is safety stock in inventory management?",
            "options": {"A": "Stock stored in secure warehouses", "B": "Extra inventory held as buffer against demand variability and supply delays to prevent stockouts", "C": "Damaged goods stored separately", "D": "Stock earmarked for export"},
            "answer": "B", "skill": "Inventory management", "level": "Beginner"
        },
        {
            "q": "EOQ (Economic Order Quantity) minimises the total of:",
            "options": {"A": "Manufacturing costs", "B": "Ordering costs and inventory holding costs combined", "C": "Transportation costs only", "D": "Supplier development costs"},
            "answer": "B", "skill": "Demand forecasting", "level": "Intermediate"
        },
        {
            "q": "A supplier scorecard tracks metrics such as:",
            "options": {"A": "Supplier CEO's biography", "B": "On-time delivery, quality (PPM defect rate), cost competitiveness, and responsiveness", "C": "Supplier's market capitalisation", "D": "Number of employees at supplier"},
            "answer": "B", "skill": "Supplier evaluation", "level": "Intermediate"
        },
        {
            "q": "In SAP, a Purchase Order (PO) is created after which document in the procurement cycle?",
            "options": {"A": "Goods Receipt (GR)", "B": "Purchase Requisition (PR) and optionally Request for Quotation (RFQ)", "C": "Invoice Verification", "D": "Payment to supplier"},
            "answer": "B", "skill": "SAP", "level": "Intermediate"
        },
        {
            "q": "Supply chain bullwhip effect refers to:",
            "options": {"A": "Price increases due to raw material shortage", "B": "Amplification of demand fluctuations as orders move upstream, causing excess inventory and stockouts", "C": "Supplier consolidation strategy", "D": "Logistics route optimisation"},
            "answer": "B", "skill": "Supply chain analytics", "level": "Intermediate"
        },
    ],

    "EV Component Buyer": [
        {
            "q": "An RFQ (Request for Quotation) is sent to suppliers to:",
            "options": {"A": "Inform suppliers of quality issues", "B": "Request detailed price quotations for specified components or services under defined technical requirements", "C": "Pay suppliers for delivered goods", "D": "Cancel existing purchase orders"},
            "answer": "B", "skill": "RFQs", "level": "Beginner"
        },
        {
            "q": "Total Cost of Ownership (TCO) analysis in procurement includes:",
            "options": {"A": "Purchase price only", "B": "Purchase price, tooling, logistics, quality costs, warranty, and end-of-life disposal", "C": "Supplier's profit margin", "D": "Market price of the component"},
            "answer": "B", "skill": "Cost analysis", "level": "Intermediate"
        },
        {
            "q": "Supplier APQP gate review ensures:",
            "options": {"A": "Supplier has paid their taxes", "B": "Supplier's development process milestones are achieved before parts are approved for production use", "C": "Supplier's factory size meets requirements", "D": "Supplier's website is updated"},
            "answer": "B", "skill": "APQP", "level": "Intermediate"
        },
        {
            "q": "What is a long-term agreement (LTA) with a supplier?",
            "options": {"A": "A one-time purchase order", "B": "A contract locking in prices, volumes, and quality terms over multiple years to reduce procurement risk", "C": "An NDA with the supplier", "D": "A loan to the supplier"},
            "answer": "B", "skill": "Contract management", "level": "Intermediate"
        },
        {
            "q": "Category management in procurement groups similar spend items to:",
            "options": {"A": "Simplify accounting", "B": "Develop strategic sourcing strategies, leverage volume, and manage supplier relationships more effectively", "C": "Reduce number of suppliers only", "D": "Track individual purchase orders"},
            "answer": "B", "skill": "Category management", "level": "Intermediate"
        },
    ],

    "EV Product Manager": [
        {
            "q": "An OKR (Objectives and Key Results) framework differs from KPIs in that:",
            "options": {"A": "OKRs are only financial metrics", "B": "OKRs set ambitious goals (objectives) with measurable outcomes (key results), focusing on what to achieve, not just track", "C": "KPIs are only for executives", "D": "OKRs replace project plans"},
            "answer": "B", "skill": "OKR framework", "level": "Intermediate"
        },
        {
            "q": "A product roadmap communicates:",
            "options": {"A": "Day-by-day task assignments", "B": "Vision, strategic direction, and planned features/milestones over time to align stakeholders", "C": "Bug list from QA testing", "D": "Employee performance plan"},
            "answer": "B", "skill": "Product roadmaps", "level": "Beginner"
        },
        {
            "q": "In agile product development, a sprint retrospective is used to:",
            "options": {"A": "Plan the next sprint's backlog", "B": "Reflect on the team's process in the last sprint — what went well, what to improve, and action items", "C": "Demo the product to customers", "D": "Estimate story points"},
            "answer": "B", "skill": "Agile", "level": "Intermediate"
        },
        {
            "q": "User story mapping in product management helps to:",
            "options": {"A": "Create technical architecture", "B": "Visualise the user journey and organise features/stories by user activity to identify MVP scope", "C": "Document API endpoints", "D": "Define database schema"},
            "answer": "B", "skill": "User story mapping", "level": "Intermediate"
        },
        {
            "q": "What is a go-to-market (GTM) strategy for an EV charging product?",
            "options": {"A": "Vehicle routing plan", "B": "Plan defining target segments, value proposition, pricing, channels, and launch activities to bring the product to market", "C": "Manufacturing process plan", "D": "Quality testing plan"},
            "answer": "B", "skill": "Go-to-market strategy", "level": "Intermediate"
        },
    ],

    "EV Project Coordinator": [
        {
            "q": "A Gantt chart in project management shows:",
            "options": {"A": "Budget allocation", "B": "Project tasks, durations, dependencies, and schedule visually on a timeline", "C": "Team hierarchy", "D": "Risk register"},
            "answer": "B", "skill": "Scheduling", "level": "Beginner"
        },
        {
            "q": "Critical Path Method (CPM) identifies:",
            "options": {"A": "Lowest cost activities", "B": "The longest sequence of dependent tasks that determines the minimum project duration", "C": "Team with least experience", "D": "Most expensive tasks"},
            "answer": "B", "skill": "Project management", "level": "Intermediate"
        },
        {
            "q": "Change control process in project management ensures:",
            "options": {"A": "All changes are approved without review", "B": "Proposed changes are evaluated for impact on scope, cost, and timeline before being approved and documented", "C": "Changes are made immediately", "D": "Only the PM can request changes"},
            "answer": "B", "skill": "Change control", "level": "Intermediate"
        },
        {
            "q": "What does RAID log track in project management?",
            "options": {"A": "Server backup logs", "B": "Risks, Assumptions, Issues, and Dependencies", "C": "Resource allocation", "D": "Invoice payments"},
            "answer": "B", "skill": "Risk management", "level": "Intermediate"
        },
        {
            "q": "Earned Value Management (EVM) in MS Project combines:",
            "options": {"A": "HR and financial data", "B": "Scope, schedule, and cost data to measure project performance — using metrics like CPI and SPI", "C": "Quality and testing data", "D": "Customer satisfaction and NPS"},
            "answer": "B", "skill": "MS Project", "level": "Advanced"
        },
    ],

    "EV Contract Manager": [
        {
            "q": "What is a liquidated damages (LD) clause in an EV charging project contract?",
            "options": {"A": "Clause allowing buyer to cancel at any time", "B": "Pre-agreed compensation amount the contractor pays for each day of delay beyond the contracted completion date", "C": "Warranty extension clause", "D": "Payment installment schedule"},
            "answer": "B", "skill": "Contract law", "level": "Intermediate"
        },
        {
            "q": "SLA (Service Level Agreement) in a charging network maintenance contract defines:",
            "options": {"A": "Software licence terms", "B": "Performance standards including uptime guarantees, response times, and penalties for non-compliance", "C": "Hardware specifications", "D": "Employee benefits"},
            "answer": "B", "skill": "SLA management", "level": "Intermediate"
        },
        {
            "q": "An NDA (Non-Disclosure Agreement) in EV technology partnerships protects:",
            "options": {"A": "Employee salaries", "B": "Confidential technical information, trade secrets, and IP shared between parties during collaboration", "C": "Physical assets", "D": "Customer payment data"},
            "answer": "B", "skill": "IP agreements", "level": "Beginner"
        },
        {
            "q": "Indemnity clauses in contracts allocate:",
            "options": {"A": "Revenue sharing between parties", "B": "Responsibility for losses, damages, or liabilities that one party causes to the other", "C": "Delivery schedules", "D": "Payment currency"},
            "answer": "B", "skill": "Contract law", "level": "Advanced"
        },
        {
            "q": "ERP contract management modules help with:",
            "options": {"A": "Email marketing", "B": "Centralised contract repository, renewal alerts, obligation tracking, and compliance monitoring", "C": "Vehicle GPS tracking", "D": "Battery chemistry analysis"},
            "answer": "B", "skill": "ERP", "level": "Intermediate"
        },
    ],

    "EV Fleet Manager": [
        {
            "q": "What is the most important metric for EV fleet total cost optimisation?",
            "options": {"A": "Vehicle colour", "B": "Cost per kilometre (CPK) — including energy, maintenance, depreciation, and insurance", "C": "Number of vehicles in fleet", "D": "Driver height"},
            "answer": "B", "skill": "Fleet economics", "level": "Intermediate"
        },
        {
            "q": "Fleet charging scheduling software optimises charging to:",
            "options": {"A": "Charge all vehicles at peak tariff hours", "B": "Ensure all vehicles are charged for next shift while minimising energy cost using off-peak tariffs and smart scheduling", "C": "Reduce number of chargers needed to zero", "D": "Extend vehicle warranty"},
            "answer": "B", "skill": "Fleet optimization", "level": "Intermediate"
        },
        {
            "q": "What ELD (Electronic Logging Device) records in commercial EV fleet operations?",
            "options": {"A": "Vehicle colour and registration", "B": "Driver hours of service (HoS) to ensure compliance with driving time regulations", "C": "Battery chemistry data", "D": "OCPP session data"},
            "answer": "B", "skill": "ELD compliance", "level": "Beginner"
        },
        {
            "q": "Preventive maintenance scheduling for EV fleet based on telematics triggers service when:",
            "options": {"A": "Driver complains", "B": "Mileage, operating hours, or sensor alerts reach predefined thresholds — before failure occurs", "C": "Battery reaches 0%", "D": "Fixed calendar date regardless of usage"},
            "answer": "B", "skill": "Maintenance planning", "level": "Intermediate"
        },
        {
            "q": "Utilisation rate of an EV fleet is calculated as:",
            "options": {"A": "Total fleet size / charging points", "B": "Actual operating hours or distance / available operating hours or distance capacity", "C": "Revenue / total vehicles", "D": "Charged kWh / battery capacity"},
            "answer": "B", "skill": "Fleet KPIs", "level": "Intermediate"
        },
    ],

    "EV Fleet Safety Manager": [
        {
            "q": "A driver risk scoring system in fleet telematics typically flags:",
            "options": {"A": "Drivers who play music", "B": "Harsh braking, rapid acceleration, speeding, and mobile phone usage events", "C": "Drivers who charge frequently", "D": "Drivers who prefer specific routes"},
            "answer": "B", "skill": "Driver safety", "level": "Intermediate"
        },
        {
            "q": "Post-incident review (PIR) in fleet safety management aims to:",
            "options": {"A": "Assign blame to drivers", "B": "Identify root causes of incidents and implement corrective actions to prevent recurrence", "C": "Calculate insurance premium changes", "D": "Report to police only"},
            "answer": "B", "skill": "Incident management", "level": "Intermediate"
        },
        {
            "q": "What is a safe system approach in road safety management?",
            "options": {"A": "Training drivers to be more careful only", "B": "Designing the entire road transport system so humans and vehicles interact safely, accounting for human error", "C": "Installing more traffic cameras", "D": "Increasing vehicle top speed limits"},
            "answer": "B", "skill": "Safety management", "level": "Advanced"
        },
        {
            "q": "Fleet safety compliance audit verifies:",
            "options": {"A": "Fleet revenue targets", "B": "Adherence to safety policies, regulations, driver licence validity, vehicle roadworthiness, and inspection records", "C": "Customer satisfaction scores", "D": "Marketing ROI"},
            "answer": "B", "skill": "Safety audits", "level": "Intermediate"
        },
        {
            "q": "Telematics-based insurance (UBI — Usage Based Insurance) for EV fleets prices premiums based on:",
            "options": {"A": "Vehicle age only", "B": "Actual driving behaviour data — mileage, time of day, speed, and driving style", "C": "Fleet size only", "D": "Brand of EV"},
            "answer": "B", "skill": "Telematics", "level": "Intermediate"
        },
    ],

    "EV Chief Innovation Officer": [
        {
            "q": "What is an innovation funnel in product development?",
            "options": {"A": "A physical component in EVs", "B": "A process that generates many ideas, progressively filters and develops the most promising ones into viable products", "C": "A financial model", "D": "A marketing campaign structure"},
            "answer": "B", "skill": "Innovation management", "level": "Intermediate"
        },
        {
            "q": "Technology Readiness Level (TRL) 9 indicates:",
            "options": {"A": "Concept on paper", "B": "Technology proven in operational environment — actual system deployed in real-world conditions", "C": "Laboratory prototype", "D": "Technology in active development"},
            "answer": "B", "skill": "Technology strategy", "level": "Advanced"
        },
        {
            "q": "Open innovation in the EV ecosystem means:",
            "options": {"A": "Sharing all IP publicly with no restrictions", "B": "Collaborating with external partners (startups, universities, suppliers) to co-develop and share innovations", "C": "Open sourcing all software", "D": "Hiring from open market only"},
            "answer": "B", "skill": "Innovation strategy", "level": "Intermediate"
        },
        {
            "q": "A technology roadmap for an EV company aligns:",
            "options": {"A": "HR recruitment with finance", "B": "Technology development plans with business strategy, market timing, and product roadmaps", "C": "Marketing calendar with sales targets", "D": "Regulatory calendar with finance"},
            "answer": "B", "skill": "Technology roadmap", "level": "Intermediate"
        },
        {
            "q": "Disruptive innovation theory (Christensen) predicts that EVs disrupted ICE vehicles by initially:",
            "options": {"A": "Outperforming ICE vehicles on every metric", "B": "Targeting niche or underserved segments (short range, city use) before improving to compete in mainstream market", "C": "Being cheaper than ICE vehicles from day one", "D": "Being mandated by regulations immediately"},
            "answer": "B", "skill": "Innovation theory", "level": "Advanced"
        },
    ],

    # =========================================================================
    # FINANCE & BUSINESS
    # =========================================================================

    "EV Finance Analyst": [
        {
            "q": "In DCF valuation, what does the terminal value represent?",
            "options": {"A": "Revenue in year 1", "B": "Present value of all cash flows beyond the explicit forecast period, often the largest component of total value", "C": "Cost of debt", "D": "Working capital adjustment"},
            "answer": "B", "skill": "DCF analysis", "level": "Advanced"
        },
        {
            "q": "WACC (Weighted Average Cost of Capital) is used as the discount rate in DCF because:",
            "options": {"A": "It is set by the central bank", "B": "It represents the minimum return required by both debt and equity investors, blended by capital structure weights", "C": "It equals the risk-free rate", "D": "It measures revenue growth"},
            "answer": "B", "skill": "Financial modeling", "level": "Advanced"
        },
        {
            "q": "EV-specific TCO (Total Cost of Ownership) is lower than ICE TCO mainly due to:",
            "options": {"A": "Lower purchase price of EVs", "B": "Lower energy cost per km, lower servicing costs (no oil, fewer moving parts), and government incentives", "C": "Lower insurance costs only", "D": "Lower financing interest rates"},
            "answer": "B", "skill": "TCO modeling", "level": "Intermediate"
        },
        {
            "q": "A sensitivity table in a financial model shows:",
            "options": {"A": "Employee satisfaction ratings", "B": "How a key output (e.g., NPV) changes as two key input assumptions vary simultaneously", "C": "Historical stock prices", "D": "Customer churn rate"},
            "answer": "B", "skill": "Scenario analysis", "level": "Intermediate"
        },
        {
            "q": "Power BI's DAX (Data Analysis Expressions) is used to:",
            "options": {"A": "Design visual layouts", "B": "Create calculated columns, measures, and tables using formula expressions in data models", "C": "Connect to external APIs", "D": "Generate PDF reports"},
            "answer": "B", "skill": "Power BI", "level": "Intermediate"
        },
    ],

    "EV Infrastructure Economist": [
        {
            "q": "A cost-benefit analysis (CBA) of public EV charging infrastructure quantifies:",
            "options": {"A": "Charger colour preferences", "B": "All costs (capex, opex, social costs) versus all benefits (emission savings, economic activity, fuel savings) in monetary terms", "C": "Number of charger brands available", "D": "Average driver age"},
            "answer": "B", "skill": "Cost-benefit analysis", "level": "Intermediate"
        },
        {
            "q": "What is the social cost of carbon (SCC) used for in EV policy analysis?",
            "options": {"A": "Calculating battery cell prices", "B": "Monetising the economic damages of emitting one additional tonne of CO2, used to justify EV subsidies", "C": "Measuring road congestion", "D": "Setting electricity tariffs"},
            "answer": "B", "skill": "Policy economics", "level": "Advanced"
        },
        {
            "q": "Network externalities in EV charging infrastructure mean:",
            "options": {"A": "Charging is faster on internet-connected chargers", "B": "The value of charging infrastructure increases as more users and vehicles join the network (virtuous cycle)", "C": "Chargers slow down when many are connected", "D": "Networks require external funding"},
            "answer": "B", "skill": "Economic theory", "level": "Advanced"
        },
        {
            "q": "Break-even analysis for a charging station determines:",
            "options": {"A": "Maximum charging speed", "B": "The utilisation rate / number of sessions needed for revenue to cover all fixed and variable costs", "C": "Optimal connector type", "D": "Grid connection voltage"},
            "answer": "B", "skill": "Financial modeling", "level": "Intermediate"
        },
        {
            "q": "What does an econometric forecasting model for EV adoption typically use as independent variables?",
            "options": {"A": "Vehicle colour and brand", "B": "Fuel prices, EV purchase price, charging infrastructure density, income levels, and policy incentives", "C": "Social media sentiment only", "D": "Weather data only"},
            "answer": "B", "skill": "Forecasting", "level": "Advanced"
        },
    ],

    "EV Business Development Lead": [
        {
            "q": "A BATNA (Best Alternative to a Negotiated Agreement) in EV partnership negotiations is important because:",
            "options": {"A": "It is a legal requirement", "B": "Knowing your best alternative strengthens negotiating position and helps decide when to walk away from a deal", "C": "It is the first offer made", "D": "It replaces the contract"},
            "answer": "B", "skill": "Negotiation", "level": "Advanced"
        },
        {
            "q": "TAM, SAM, and SOM in market sizing for EV charging products refer to:",
            "options": {"A": "Types of chargers", "B": "Total Addressable Market, Serviceable Addressable Market, and Serviceable Obtainable Market — sizing the market opportunity", "C": "Technical standards", "D": "Battery chemistry grades"},
            "answer": "B", "skill": "Market research", "level": "Intermediate"
        },
        {
            "q": "A MOU (Memorandum of Understanding) in an EV partnership:",
            "options": {"A": "Is a legally binding contract", "B": "Outlines the intent to collaborate, key terms, and scope — typically non-binding but establishes framework for negotiations", "C": "Transfers IP rights immediately", "D": "Is a purchase order"},
            "answer": "B", "skill": "Partnership development", "level": "Intermediate"
        },
        {
            "q": "Customer Lifetime Value (CLV) in a charging network business model estimates:",
            "options": {"A": "Vehicle resale value", "B": "Total revenue a customer generates over their relationship with the charging network", "C": "Battery degradation cost", "D": "Individual session revenue only"},
            "answer": "B", "skill": "Business strategy", "level": "Intermediate"
        },
        {
            "q": "Salesforce CRM pipeline management tracks:",
            "options": {"A": "Battery inventory", "B": "Lead status, deal stages, probability of close, and expected revenue across active opportunities", "C": "Fleet maintenance schedule", "D": "Employee performance reviews"},
            "answer": "B", "skill": "Salesforce CRM", "level": "Intermediate"
        },
    ],

    "EV Sales Specialist": [
        {
            "q": "When explaining EV TCO to a fleet customer hesitating due to high upfront cost, you should emphasise:",
            "options": {"A": "Vehicle aesthetics", "B": "Lower energy costs, reduced maintenance, government subsidies, and that TCO is typically lower than ICE over 3–5 years", "C": "Higher top speed", "D": "Charging time only"},
            "answer": "B", "skill": "EV product knowledge", "level": "Intermediate"
        },
        {
            "q": "SPIN selling technique stands for:",
            "options": {"A": "Speed, Price, Interest, Need", "B": "Situation, Problem, Implication, Need-Payoff — a consultative questioning approach to uncover customer needs", "C": "Sales, Performance, Integration, Network", "D": "Service, Product, Investment, Negotiation"},
            "answer": "B", "skill": "Sales technique", "level": "Intermediate"
        },
        {
            "q": "FAME II subsidy benefit is most relevant to highlight when selling to:",
            "options": {"A": "Premium private car buyers", "B": "Fleet operators, e-commerce delivery companies, and public transport operators who qualify for maximum subsidy", "C": "Luxury EV buyers", "D": "International customers"},
            "answer": "B", "skill": "Government incentives", "level": "Intermediate"
        },
        {
            "q": "What is a key objection handling technique when a customer says 'EVs have too little range'?",
            "options": {"A": "Agree and recommend ICE vehicles", "B": "Acknowledge concern, then provide real-world range data, show charging infrastructure map, and share fleet case studies", "C": "Ignore the concern", "D": "Offer to reduce the price"},
            "answer": "B", "skill": "Objection handling", "level": "Intermediate"
        },
        {
            "q": "A CRM system is used in EV sales to:",
            "options": {"A": "Design the EV battery", "B": "Track leads, customer interactions, follow-ups, deal stages, and sales pipeline to manage the sales process", "C": "Calculate energy consumption", "D": "Programme the BMS"},
            "answer": "B", "skill": "CRM", "level": "Beginner"
        },
    ],

    "EV Marketing Strategist": [
        {
            "q": "In EV marketing, what does 'range anxiety' content strategy aim to achieve?",
            "options": {"A": "Increase anxiety to boost sales urgency", "B": "Educate and reassure potential buyers with real-world range data, charging infrastructure maps, and user testimonials", "C": "Avoid mentioning range", "D": "Promote only fast charging"},
            "answer": "B", "skill": "Content marketing", "level": "Intermediate"
        },
        {
            "q": "Google Ads Quality Score affects:",
            "options": {"A": "Ad creative size", "B": "Ad rank and cost-per-click — higher quality score = better placement at lower cost", "C": "Campaign budget", "D": "Number of keywords"},
            "answer": "B", "skill": "Google Ads", "level": "Intermediate"
        },
        {
            "q": "What is SEO canonical tag used for?",
            "options": {"A": "Track website visitors", "B": "Tell search engines which URL is the preferred version when duplicate or similar content exists on multiple URLs", "C": "Speed up page loading", "D": "Enable social sharing"},
            "answer": "B", "skill": "SEO", "level": "Advanced"
        },
        {
            "q": "A/B testing in EV product landing pages tests:",
            "options": {"A": "Two different battery chemistries", "B": "Two versions of a page element (headline, CTA, image) to determine which drives higher conversion rates", "C": "Two charging protocols", "D": "Two pricing models simultaneously with all users"},
            "answer": "B", "skill": "A/B testing", "level": "Intermediate"
        },
        {
            "q": "Brand positioning for an EV company in a competitive market defines:",
            "options": {"A": "Vehicle colour palette", "B": "How the brand wants to be perceived relative to competitors in the minds of target customers", "C": "Distribution network size", "D": "Manufacturing location"},
            "answer": "B", "skill": "Branding", "level": "Intermediate"
        },
    ],

    "EV After-Sales Support Engineer": [
        {
            "q": "Remote diagnostics for an EV in the field can retrieve which type of data?",
            "options": {"A": "Driver's personal data", "B": "DTC (Diagnostic Trouble Codes), live sensor data, BMS parameters, and OTA update status", "C": "Vehicle insurance details", "D": "Traffic camera footage"},
            "answer": "B", "skill": "Remote diagnostics", "level": "Intermediate"
        },
        {
            "q": "What is an escalation matrix in technical support?",
            "options": {"A": "Vehicle speed ramp function", "B": "Defined process for escalating unresolved issues from Tier 1 to Tier 2 to engineering based on severity and time", "C": "Staircase design in service centres", "D": "Price escalation policy"},
            "answer": "B", "skill": "Support process", "level": "Intermediate"
        },
        {
            "q": "Telematics data is used in after-sales support to:",
            "options": {"A": "Monitor driving for insurance only", "B": "Proactively identify vehicles approaching failure conditions and schedule service before breakdown", "C": "Track vehicle location for marketing", "D": "Measure cabin air quality only"},
            "answer": "B", "skill": "Telematics", "level": "Intermediate"
        },
        {
            "q": "A technical service bulletin (TSB) is issued to service centres to:",
            "options": {"A": "Announce new product launches", "B": "Communicate known issues, updated repair procedures, or software fixes for specific vehicle models", "C": "Invite customers for test drives", "D": "Update pricing"},
            "answer": "B", "skill": "Technical documentation", "level": "Beginner"
        },
        {
            "q": "Mean Time To Respond (MTTR) in customer support SLAs measures:",
            "options": {"A": "Average repair time", "B": "Time from customer report to first acknowledgement and initial response from support team", "C": "Time to manufacture a part", "D": "Time to close the ticket only"},
            "answer": "B", "skill": "SLA management", "level": "Beginner"
        },
    ],

    "EV Tech Support Specialist": [
        {
            "q": "Tier 1 technical support handles:",
            "options": {"A": "Complex hardware repairs", "B": "First-contact resolution of common issues using knowledge base, remote access, and standard troubleshooting scripts", "C": "New product development", "D": "Root cause analysis for systemic failures"},
            "answer": "B", "skill": "Support tiers", "level": "Beginner"
        },
        {
            "q": "When remotely troubleshooting a charger that shows 'Unavailable' in OCPP backend, first step is:",
            "options": {"A": "Replace the charger", "B": "Check network connectivity, verify OCPP WebSocket connection status, and review charger logs for disconnection reason", "C": "Schedule a physical visit immediately", "D": "Reset the customer's account"},
            "answer": "B", "skill": "OCPP troubleshooting", "level": "Intermediate"
        },
        {
            "q": "A knowledge base in tech support is valuable because:",
            "options": {"A": "It replaces support agents", "B": "It documents solutions to common problems, enabling faster resolution and self-service for repeat issues", "C": "It stores customer payment data", "D": "It tracks charger locations"},
            "answer": "B", "skill": "Knowledge management", "level": "Beginner"
        },
        {
            "q": "Python scripting in EV tech support can be used to:",
            "options": {"A": "Design vehicle body", "B": "Automate log parsing, send bulk OCPP commands, and analyse charger fault data across the network", "C": "Train ML models for new products", "D": "Design charging hardware"},
            "answer": "B", "skill": "Python", "level": "Intermediate"
        },
        {
            "q": "What information should always be collected at the start of a support ticket for an EV charging issue?",
            "options": {"A": "Customer's age", "B": "Charger ID, location, error code/description, time of occurrence, and steps already taken by customer", "C": "Customer's vehicle colour", "D": "Customer's payment history"},
            "answer": "B", "skill": "Support process", "level": "Beginner"
        },
    ],

    "EV Customer Experience Analyst": [
        {
            "q": "Customer Effort Score (CES) measures:",
            "options": {"A": "How much the company spent on customer service", "B": "How easy or difficult customers found it to complete a task or resolve an issue", "C": "Customer's physical effort during test drive", "D": "Number of customer complaints"},
            "answer": "B", "skill": "CX metrics", "level": "Intermediate"
        },
        {
            "q": "Sentiment analysis on EV charging app reviews uses NLP to:",
            "options": {"A": "Count total reviews", "B": "Automatically classify customer feedback as positive, negative, or neutral to identify common pain points at scale", "C": "Respond to all reviews", "D": "Translate reviews to English"},
            "answer": "B", "skill": "Data analysis", "level": "Intermediate"
        },
        {
            "q": "A customer journey map in EV charging service design identifies:",
            "options": {"A": "Vehicle route on GPS", "B": "All touchpoints and emotions a customer experiences from discovering a charger to completing a session and payment", "C": "Cable routing in the charger", "D": "Charging speed profile"},
            "answer": "B", "skill": "Customer journey", "level": "Intermediate"
        },
        {
            "q": "Cohort analysis in EV app analytics groups users by:",
            "options": {"A": "Vehicle brand", "B": "Shared characteristic (e.g., sign-up month) to track behaviour and retention patterns over time for each group", "C": "Geographical location only", "D": "Session energy consumed"},
            "answer": "B", "skill": "Analytics", "level": "Advanced"
        },
        {
            "q": "Voice of Customer (VoC) programme in a charging network collects feedback through:",
            "options": {"A": "Internal employee reviews", "B": "Surveys, interviews, support tickets, app reviews, and social media to capture customer needs and pain points", "C": "Technical performance logs only", "D": "Financial reports"},
            "answer": "B", "skill": "VoC", "level": "Beginner"
        },
    ],

    "EV Remote Support Technician": [
        {
            "q": "When accessing a charger remotely via OCPP backend, which action can restart a frozen transaction?",
            "options": {"A": "Heartbeat message", "B": "Remote Stop Transaction + Reset command via OCPP ChangeAvailability or Reset request", "C": "MeterValues request", "D": "StatusNotification polling"},
            "answer": "B", "skill": "OCPP", "level": "Advanced"
        },
        {
            "q": "What tool is commonly used to remotely access and control a charger's embedded Linux system for deep diagnostics?",
            "options": {"A": "Bluetooth pairing", "B": "SSH (Secure Shell) over the charger's secure network connection", "C": "USB cable directly", "D": "OCPP DataTransfer message"},
            "answer": "B", "skill": "Remote diagnostics", "level": "Intermediate"
        },
        {
            "q": "OBD-II remote monitoring of an EV can report:",
            "options": {"A": "Driver's fingerprint", "B": "Active DTCs, freeze frame data, live sensor PIDs, and readiness monitors", "C": "Vehicle exterior colour", "D": "Road surface condition"},
            "answer": "B", "skill": "OBD-II", "level": "Intermediate"
        },
        {
            "q": "When a remote support technician identifies a recurring fault code across multiple vehicles in a fleet, the correct action is:",
            "options": {"A": "Ignore if vehicles still work", "B": "Document the pattern, escalate to engineering as a potential systemic issue, and initiate root cause analysis", "C": "Close all tickets immediately", "D": "Only inform the driver"},
            "answer": "B", "skill": "Escalation", "level": "Intermediate"
        },
        {
            "q": "CRM ticket categorisation in EV remote support helps:",
            "options": {"A": "Sort tickets alphabetically", "B": "Track issue types, identify recurring problems, measure resolution times, and generate service quality reports", "C": "Assign tickets by driver name", "D": "Calculate support team salary"},
            "answer": "B", "skill": "CRM", "level": "Beginner"
        },
    ],

    "EV Repair Technician": [
        {
            "q": "Before working on any EV high-voltage system, what is the mandatory first step?",
            "options": {"A": "Check tyre pressure", "B": "Switch off the vehicle, engage the service disconnect (manual service disconnect/MSD), and verify HV isolation with a voltmeter", "C": "Remove the wheels", "D": "Connect the OBD scanner"},
            "answer": "B", "skill": "HV safety", "level": "Beginner"
        },
        {
            "q": "An OBD-II scan tool reads a DTC P0A80 on an EV. This typically indicates:",
            "options": {"A": "Tyre pressure sensor fault", "B": "Replace Hybrid/EV Battery Pack — battery system degradation or fault detected by BMS", "C": "Engine misfire", "D": "ABS fault"},
            "answer": "B", "skill": "EV diagnostics", "level": "Intermediate"
        },
        {
            "q": "Cell voltage imbalance in an EV battery pack during repair diagnosis indicates:",
            "options": {"A": "Normal pack condition", "B": "One or more cells are degraded, have higher internal resistance, or there is a BMS balancing fault", "C": "Charger fault", "D": "Motor controller fault"},
            "answer": "B", "skill": "Battery diagnostics", "level": "Intermediate"
        },
        {
            "q": "What colour coding system is used universally for high-voltage components and wiring in EVs?",
            "options": {"A": "Red and black", "B": "Orange (FMVSS 305 / OEM standard) for HV cables and components", "C": "Yellow and green", "D": "Blue for positive, white for negative"},
            "answer": "B", "skill": "HV safety", "level": "Beginner"
        },
        {
            "q": "After replacing an EV battery module, the BMS must be recalibrated to:",
            "options": {"A": "Reset the odometer", "B": "Update the pack configuration, recalculate SOH baseline, and re-enable cell balancing for the new module", "C": "Reset the infotainment system", "D": "Reprogram the ABS module"},
            "answer": "B", "skill": "BMS", "level": "Advanced"
        },
    ],

    "EV Warranty Analyst": [
        {
            "q": "Warranty accrual accounting requires manufacturers to:",
            "options": {"A": "Pay all claims immediately without provisions", "B": "Estimate and book a liability reserve at time of sale based on expected future warranty costs", "C": "Charge warranty costs to R&D budget", "D": "Record only actual claims paid"},
            "answer": "B", "skill": "Warranty accounting", "level": "Intermediate"
        },
        {
            "q": "An 8D report in warranty root cause analysis requires:",
            "options": {"A": "8 different engineers to sign", "B": "8 structured steps: Define team, describe problem, interim containment, root cause, permanent corrective actions, verification, prevention, congratulate team", "C": "8 weeks to complete", "D": "8 data sources"},
            "answer": "B", "skill": "8D methodology", "level": "Intermediate"
        },
        {
            "q": "Supplier chargeback in warranty claims means:",
            "options": {"A": "Supplier charges OEM for testing", "B": "OEM recovers warranty repair costs from the responsible component supplier when the root cause is traced to their part", "C": "Customer is charged for warranty", "D": "Government reimburses warranty costs"},
            "answer": "B", "skill": "Supplier recovery", "level": "Advanced"
        },
        {
            "q": "ANOVA (Analysis of Variance) in warranty data analysis tests:",
            "options": {"A": "Whether all data is normally distributed", "B": "Whether failure rates differ significantly across production batches, regions, or vehicle configurations", "C": "Correlation between two variables", "D": "Time series trends"},
            "answer": "B", "skill": "Statistical analysis", "level": "Advanced"
        },
        {
            "q": "Warranty period start date for an EV battery is typically triggered by:",
            "options": {"A": "Date of battery manufacturing", "B": "Date of vehicle first registration / delivery to end customer (in-service date)", "C": "Date of dealer purchase from OEM", "D": "Date of first charge"},
            "answer": "B", "skill": "Warranty policy", "level": "Beginner"
        },
    ],

    "EV Warranty Claims Technician": [
        {
            "q": "What must be verified first when processing an EV warranty claim?",
            "options": {"A": "Customer's credit score", "B": "Vehicle VIN, purchase date, and whether the reported failure is within warranty coverage period and terms", "C": "Dealership revenue", "D": "Vehicle exterior condition only"},
            "answer": "B", "skill": "Claims validation", "level": "Beginner"
        },
        {
            "q": "A warranty claim for battery capacity degradation is typically valid when:",
            "options": {"A": "Customer notices any range difference", "B": "Battery SOH falls below the OEM-specified threshold (e.g., 70% of original capacity) within the warranty period", "C": "Battery is over 1 year old", "D": "Charging speed decreases slightly"},
            "answer": "B", "skill": "Warranty policy", "level": "Intermediate"
        },
        {
            "q": "Parts return management in warranty requires returned parts to be:",
            "options": {"A": "Immediately discarded", "B": "Tagged with claim reference, stored per OEM requirements, and analysed by engineering if required for root cause", "C": "Resold to secondary market", "D": "Returned to customer"},
            "answer": "B", "skill": "Parts return", "level": "Intermediate"
        },
        {
            "q": "What SAP transaction code is typically used to create a warranty claim notification?",
            "options": {"A": "MM01", "B": "IW51 or CS transaction for customer notification / service order creation", "C": "FI01", "D": "HR01"},
            "answer": "B", "skill": "SAP", "level": "Advanced"
        },
        {
            "q": "When a claim is rejected, what must the warranty claims technician provide to the customer?",
            "options": {"A": "A discount voucher", "B": "Written explanation of the rejection reason citing the specific warranty exclusion or out-of-scope condition", "C": "Alternative vehicle", "D": "Refund of purchase price"},
            "answer": "B", "skill": "Warranty process", "level": "Intermediate"
        },
    ],

    "EV Warranty Program Manager": [
        {
            "q": "What is the purpose of a warranty reserve model?",
            "options": {"A": "Track spare parts inventory", "B": "Forecast future warranty costs based on fleet size, failure rates, and repair costs to ensure adequate financial provisions", "C": "Manage dealer incentives", "D": "Track customer NPS"},
            "answer": "B", "skill": "Warranty forecasting", "level": "Advanced"
        },
        {
            "q": "Early life failure (ELF) in a warranty programme refers to:",
            "options": {"A": "Failures after 10 years", "B": "Failures occurring disproportionately early in a product's life, often due to manufacturing defects (infant mortality)", "C": "Battery end-of-life", "D": "Customer misuse"},
            "answer": "B", "skill": "Reliability", "level": "Intermediate"
        },
        {
            "q": "A warranty dashboard KPI showing 'cost per unit in operation (CPUIO)' tracks:",
            "options": {"A": "Revenue per vehicle", "B": "Average warranty cost incurred per vehicle in the operating fleet per year — key efficiency metric", "C": "Number of service centres", "D": "Sales per region"},
            "answer": "B", "skill": "Warranty KPIs", "level": "Intermediate"
        },
        {
            "q": "Field action (recall) decision in warranty management is triggered when:",
            "options": {"A": "A single vehicle has a complaint", "B": "A systemic safety or compliance issue is confirmed affecting a population of vehicles, requiring mandatory corrective action", "C": "Annual warranty review suggests cost reduction", "D": "Media reports about a competitor"},
            "answer": "B", "skill": "Field action", "level": "Advanced"
        },
        {
            "q": "Warranty program harmonisation across global markets addresses:",
            "options": {"A": "Colour standardisation", "B": "Different warranty terms, periods, and coverage by region due to local regulations, consumer protection laws, and market expectations", "C": "Voltage standardisation", "D": "Language translation only"},
            "answer": "B", "skill": "Warranty policy", "level": "Intermediate"
        },
    ],

    # =========================================================================
    # TRAINING & MANUFACTURING
    # =========================================================================

    "EV Technician Trainer": [
        {
            "q": "Bloom's Taxonomy highest level (evaluation/synthesis) in EV training design means learners can:",
            "options": {"A": "Recall facts from memory", "B": "Critically assess and create — e.g., diagnose an unfamiliar EV fault using systematic principles, not just a checklist", "C": "Follow a procedure step-by-step", "D": "Recognise components by sight"},
            "answer": "B", "skill": "Instructional design", "level": "Advanced"
        },
        {
            "q": "70-20-10 learning model in EV technician training suggests:",
            "options": {"A": "Equal split of theory, practical, and assessment", "B": "70% on-the-job experience, 20% coaching/mentoring, 10% formal training — learning primarily through doing", "C": "10 modules with 70% pass mark", "D": "70 hours classroom, 20 hours lab, 10 hours exam"},
            "answer": "B", "skill": "Training methodology", "level": "Intermediate"
        },
        {
            "q": "ASE (Automotive Service Excellence) certification relevance for EV technicians includes:",
            "options": {"A": "Only ICE engine repair", "B": "EV-specific certifications (L3 for EVs) validating knowledge and competency for hybrid and electric vehicle service", "C": "Sales training", "D": "Manufacturing quality"},
            "answer": "B", "skill": "Certification", "level": "Intermediate"
        },
        {
            "q": "A learning management system (LMS) like Moodle enables trainers to:",
            "options": {"A": "Design vehicle body panels", "B": "Deliver, track, and assess online training courses, manage learner progress, and generate completion reports", "C": "Monitor fleet telematics", "D": "Process warranty claims"},
            "answer": "B", "skill": "LMS platforms", "level": "Beginner"
        },
        {
            "q": "Formative assessment in EV technician training is used:",
            "options": {"A": "Only at course end for certification", "B": "During training to provide ongoing feedback and identify knowledge gaps before they become entrenched", "C": "To rank trainees competitively", "D": "To measure training ROI"},
            "answer": "B", "skill": "Assessment design", "level": "Intermediate"
        },
    ],

    "EV Training Content Developer": [
        {
            "q": "SCORM (Sharable Content Object Reference Model) is important in eLearning because:",
            "options": {"A": "It defines battery chemistry", "B": "It is a technical standard ensuring eLearning content works across different LMS platforms and tracks learner data", "C": "It is a vehicle safety standard", "D": "It specifies video resolution"},
            "answer": "B", "skill": "eLearning standards", "level": "Intermediate"
        },
        {
            "q": "Articulate Storyline 360 is used primarily to create:",
            "options": {"A": "CAD drawings", "B": "Interactive eLearning modules with branching scenarios, quizzes, and multimedia for delivery on LMS", "C": "Financial reports", "D": "Database queries"},
            "answer": "B", "skill": "eLearning development", "level": "Intermediate"
        },
        {
            "q": "A SME (Subject Matter Expert) in training content development is involved to:",
            "options": {"A": "Design the visual theme", "B": "Provide accurate technical content, review material for correctness, and validate learning objectives", "C": "Programme the LMS", "D": "Record voice-over narration"},
            "answer": "B", "skill": "Content development", "level": "Beginner"
        },
        {
            "q": "Kirkpatrick Level 4 in training evaluation measures:",
            "options": {"A": "Learner satisfaction with content", "B": "Business results — whether the training improved organisational performance indicators like productivity or safety incidents", "C": "Knowledge gained during training", "D": "Trainer delivery quality"},
            "answer": "B", "skill": "Training evaluation", "level": "Advanced"
        },
        {
            "q": "A storyboard in eLearning content development serves as:",
            "options": {"A": "Final published course", "B": "Detailed blueprint showing each slide's content, visuals, narration, interactions, and branching before development begins", "C": "Marketing brochure", "D": "Technical specification for hardware"},
            "answer": "B", "skill": "Instructional design", "level": "Intermediate"
        },
    ],

    "EV Robotics Technician": [
        {
            "q": "In EV battery pack assembly automation, what is the primary role of a FANUC or KUKA articulated robot?",
            "options": {"A": "Monitor BMS parameters", "B": "Perform precise, repeatable material handling, welding, or assembly tasks at speeds and accuracy exceeding manual capability", "C": "Design battery architecture", "D": "Flash firmware to ECUs"},
            "answer": "B", "skill": "Robotics", "level": "Beginner"
        },
        {
            "q": "PLC (Programmable Logic Controller) ladder logic is a programming language that resembles:",
            "options": {"A": "Python syntax", "B": "Relay logic diagrams — using contacts (inputs) and coils (outputs) for industrial control applications", "C": "SQL queries", "D": "HTML markup"},
            "answer": "B", "skill": "PLC programming", "level": "Intermediate"
        },
        {
            "q": "Robot TCP (Tool Centre Point) calibration is performed to:",
            "options": {"A": "Update robot firmware", "B": "Precisely define the location of the end-effector tip relative to the robot flange for accurate path execution", "C": "Programme robot speed", "D": "Set robot safe zones"},
            "answer": "B", "skill": "Robot calibration", "level": "Intermediate"
        },
        {
            "q": "Safety fencing and light curtains around EV assembly robots provide:",
            "options": {"A": "Better viewing angle for operators", "B": "Physical and electronic barriers that stop robot motion immediately when humans enter the hazard zone", "C": "Temperature protection for robots", "D": "EMI shielding"},
            "answer": "B", "skill": "Safety", "level": "Beginner"
        },
        {
            "q": "Vision system integration in a battery assembly robot enables:",
            "options": {"A": "Robot to see colour", "B": "Precise part location, quality inspection (weld quality, presence/absence), and adaptive path correction", "C": "Network communication", "D": "Wireless firmware update"},
            "answer": "B", "skill": "Vision systems", "level": "Advanced"
        },
    ],

    "Hydrogen Fuel Cell Engineer": [
        {
            "q": "In a PEM (Proton Exchange Membrane) fuel cell, what is the function of the membrane?",
            "options": {"A": "Catalyse the oxidation reaction", "B": "Conduct protons (H+) from anode to cathode while blocking electron flow and being impermeable to gases", "C": "Store hydrogen under pressure", "D": "Regulate operating temperature"},
            "answer": "B", "skill": "PEM fuel cell", "level": "Intermediate"
        },
        {
            "q": "Why is cathode flooding a degradation mechanism in PEM fuel cells?",
            "options": {"A": "Increases proton conductivity", "B": "Excess water blocks gas diffusion layer pores, preventing oxygen from reaching catalyst sites and reducing power output", "C": "Improves membrane durability", "D": "Reduces platinum loading requirement"},
            "answer": "B", "skill": "Fuel cell degradation", "level": "Advanced"
        },
        {
            "q": "Balance of Plant (BoP) in a fuel cell system includes:",
            "options": {"A": "Only the fuel cell stack", "B": "All supporting subsystems: air compressor, humidifier, cooling system, hydrogen recirculation, and power electronics", "C": "Vehicle chassis only", "D": "Battery management system"},
            "answer": "B", "skill": "Balance of plant", "level": "Intermediate"
        },
        {
            "q": "Hydrogen colour coding (green, blue, grey) refers to:",
            "options": {"A": "Hydrogen purity levels", "B": "Production method: green (renewable electrolysis), blue (natural gas + CCS), grey (natural gas without CCS)", "C": "Storage pressure levels", "D": "Vehicle compatibility"},
            "answer": "B", "skill": "Hydrogen types", "level": "Intermediate"
        },
        {
            "q": "CFD simulation of a fuel cell cooling system optimises:",
            "options": {"A": "Membrane chemical composition", "B": "Coolant flow distribution and temperature uniformity across the stack to prevent hotspots and degradation", "C": "Stack compression force", "D": "Platinum catalyst loading"},
            "answer": "B", "skill": "CFD", "level": "Advanced"
        },
    ],

    "EV Charging Site Manager": [
        {
            "q": "What is the primary KPI for a commercial EV charging site's commercial success?",
            "options": {"A": "Number of user complaints", "B": "Charger utilisation rate (sessions per charger per day × revenue per session)", "C": "Total charger count on site", "D": "Number of different connector types"},
            "answer": "B", "skill": "Site operations", "level": "Intermediate"
        },
        {
            "q": "When a DC fast charger on site shows 'Out of Order' for 3+ hours, site manager should:",
            "options": {"A": "Wait for it to self-resolve", "B": "Escalate to maintenance team/CPO support with charger ID and fault details, and update status in OCPP backend", "C": "Reboot the entire site power", "D": "Inform customers to use competitor sites only"},
            "answer": "B", "skill": "Incident management", "level": "Intermediate"
        },
        {
            "q": "Energy management at a charging hub can reduce operating costs by:",
            "options": {"A": "Using only the fastest chargers", "B": "Shifting load to off-peak hours, using battery storage for peak shaving, and optimising solar self-consumption", "C": "Reducing number of operating hours", "D": "Installing more chargers than needed"},
            "answer": "B", "skill": "Energy management", "level": "Advanced"
        },
        {
            "q": "A charging site SLA with a landlord/property owner typically guarantees:",
            "options": {"A": "Number of EVs to be charged daily", "B": "Minimum uptime, revenue share terms, maintenance responsibilities, and branding/signage rights", "C": "Free electricity for the landlord", "D": "Specific vehicle brands served"},
            "answer": "B", "skill": "SLA management", "level": "Intermediate"
        },
        {
            "q": "Customer satisfaction at an EV charging site is most impacted by:",
            "options": {"A": "Paint colour of the charger", "B": "Charger reliability/uptime, ease of payment, clear instructions, and adequate connector availability at busy times", "C": "Background music at site", "D": "Site manager's qualifications"},
            "answer": "B", "skill": "Customer experience", "level": "Beginner"
        },
    ],

    "EV UX/UI Designer": [
        {
            "q": "In HMI design for an EV dashboard, progressive disclosure means:",
            "options": {"A": "Showing all information at once", "B": "Showing only the most critical information by default, with additional details available on demand to reduce cognitive load", "C": "Progressive colour changes", "D": "Disclosing battery chemistry to driver"},
            "answer": "B", "skill": "HMI design", "level": "Intermediate"
        },
        {
            "q": "WCAG (Web Content Accessibility Guidelines) 2.1 apply to EV charging apps to ensure:",
            "options": {"A": "Apps load faster", "B": "Users with disabilities (visual, motor, cognitive) can use the app effectively — legal requirement in many markets", "C": "App stores approve the app", "D": "Apps work on all phone brands"},
            "answer": "B", "skill": "Accessibility", "level": "Intermediate"
        },
        {
            "q": "A design system in Figma for an EV brand includes:",
            "options": {"A": "Vehicle engineering drawings", "B": "Reusable components, colour tokens, typography, spacing, and interaction patterns ensuring consistent brand expression across products", "C": "Marketing copy templates", "D": "Source code for the app"},
            "answer": "B", "skill": "Design systems", "level": "Intermediate"
        },
        {
            "q": "User testing a charging app with 5 participants follows Nielsen's rule that:",
            "options": {"A": "5 users find 5% of usability issues", "B": "5 users typically uncover ~85% of major usability problems — optimal balance of insight vs cost", "C": "You need 100+ users for statistical validity", "D": "5 users are too few to be useful"},
            "answer": "B", "skill": "Usability testing", "level": "Intermediate"
        },
        {
            "q": "Micro-interactions in an EV charging app (e.g., animated plug icon during charging) serve to:",
            "options": {"A": "Consume more battery", "B": "Provide real-time feedback confirming system state, increasing user confidence and reducing uncertainty", "C": "Meet accessibility requirements", "D": "Comply with OCPP standards"},
            "answer": "B", "skill": "UI design", "level": "Intermediate"
        },
    ],

    "Electrical Systems Engineer": [
        {
            "q": "What is LV 214 and why is it relevant in EV wiring harness design?",
            "options": {"A": "A low-voltage battery standard", "B": "Volkswagen Group's wiring harness engineering standard defining component requirements, test methods, and quality criteria", "C": "A European charging connector standard", "D": "An Indian safety regulation"},
            "answer": "B", "skill": "LV 214", "level": "Advanced"
        },
        {
            "q": "Voltage drop in an EV wiring harness is critical because:",
            "options": {"A": "It makes wires warm", "B": "Excessive drop reduces available voltage at loads, affects system performance, and can cause ECU brown-outs", "C": "It is required by ISO 26262", "D": "It determines connector colour"},
            "answer": "B", "skill": "Circuit design", "level": "Intermediate"
        },
        {
            "q": "CAN bus termination resistors (120Ω) at both ends of the bus are needed to:",
            "options": {"A": "Limit current consumption", "B": "Match the cable's characteristic impedance and prevent signal reflections that cause communication errors", "C": "Protect the CAN transceiver from ESD", "D": "Enable bus-off recovery"},
            "answer": "B", "skill": "CAN bus", "level": "Advanced"
        },
        {
            "q": "HV arc flash analysis determines the minimum PPE category for workers near live EV HV systems based on:",
            "options": {"A": "Worker's experience level", "B": "Calculated incident energy (cal/cm²) at working distance during a maximum possible arc flash event", "C": "Company policy document", "D": "Equipment manufacturer recommendation only"},
            "answer": "B", "skill": "Arc flash analysis", "level": "Advanced"
        },
        {
            "q": "In Mentor Capital (now Capital MCAD), circuit simulation before harness design allows engineers to:",
            "options": {"A": "Create 3D vehicle models", "B": "Verify electrical connectivity, detect shorts/opens, and simulate load conditions before physical prototype", "C": "Order wire from suppliers", "D": "Generate assembly work instructions"},
            "answer": "B", "skill": "Harness design tools", "level": "Intermediate"
        },
    ],

    "EV Telematics Hardware Engineer": [
        {
            "q": "GNSS (Global Navigation Satellite System) accuracy for EV telematics can be improved using:",
            "options": {"A": "Longer antenna cable", "B": "DGPS (Differential GPS) or RTK corrections reducing position error from metres to centimetres", "C": "Higher vehicle speed", "D": "More frequent GPS polling"},
            "answer": "B", "skill": "GPS", "level": "Advanced"
        },
        {
            "q": "What is the purpose of a CAN transceiver IC (e.g., TJA1051) in a telematics hardware module?",
            "options": {"A": "Process CAN messages", "B": "Convert digital logic signals from the microcontroller to/from the differential CAN bus electrical signal levels", "C": "Generate CAN bus clock", "D": "Store CAN messages in memory"},
            "answer": "B", "skill": "CAN hardware", "level": "Intermediate"
        },
        {
            "q": "LTE-M (Cat-M1) is preferred over standard LTE for telematics devices because:",
            "options": {"A": "Higher data rate", "B": "Lower power consumption, smaller module size, better building penetration, and lower cost suitable for IoT applications", "C": "Free data plans", "D": "No SIM card needed"},
            "answer": "B", "skill": "Cellular modules", "level": "Intermediate"
        },
        {
            "q": "Antenna placement on a telematics device must avoid:",
            "options": {"A": "High-traffic vehicle areas", "B": "Metal surfaces and structures that would attenuate RF signal — antennas need clear RF path and ground plane", "C": "Visible locations", "D": "Warm areas of the vehicle"},
            "answer": "B", "skill": "Antenna design", "level": "Advanced"
        },
        {
            "q": "EMC compliance testing for an EV telematics module per CISPR 25 verifies:",
            "options": {"A": "Module waterproofing", "B": "That the module's emissions do not interfere with vehicle radio receivers (AM/FM/DAB/GPS) within the vehicle", "C": "Module operating temperature range", "D": "CAN bus baud rate"},
            "answer": "B", "skill": "EMC compliance", "level": "Advanced"
        },
    ],

}



